FROM python:3.5

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

# Install uWSGI
RUN pip install uwsgi

# There is no longer an official Nginx Docker image for Debian Jessie, only for Debian Stretch,
# but the official Python 3.5 image is only available in Debian Jessie,
# so, here's an updated custom Nginx installation, based on the last official Jessie Nginx image
# Installation reference: https://www.nginx.com/resources/wiki/start/topics/tutorials/install/
# Packages repo: http://nginx.org/packages/debian/dists/jessie/
ENV NGINX_VERSION 1.15.0-1~jessie
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62 \
	&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install -y ca-certificates nginx=${NGINX_VERSION} gettext-base \
	&& rm -rf /var/lib/apt/lists/*
# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log
EXPOSE 80 443
# Finished setting up Nginx

# Make NGINX run on the foreground
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# Remove default configuration from Nginx
RUN rm /etc/nginx/conf.d/default.conf
# Copy the modified Nginx conf
COPY nginx.conf /etc/nginx/conf.d/
# Copy the base uWSGI ini file to enable default dynamic uwsgi process number
COPY uwsgi.ini /etc/uwsgi/

# Install Supervisord
RUN apt-get update && apt-get install -y supervisor \
&& rm -rf /var/lib/apt/lists/*
# Custom Supervisord config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Which uWSGI .ini file should be used, to make it customizable
ENV UWSGI_INI /app/uwsgi.ini

# By default, run 2 processes
ENV UWSGI_CHEAPER 2

# By default, when on demand, run up to 16 processes
ENV UWSGI_PROCESSES 16

# By default, allow unlimited file sizes, modify it to limit the file sizes
# To have a maximum of 1 MB (Nginx's default) change the line to:
# ENV NGINX_MAX_UPLOAD 1m
ENV NGINX_MAX_UPLOAD 0

# By default, Nginx will run a single worker process, setting it to auto
# will create a worker for each CPU core
ENV NGINX_WORKER_PROCESSES 1

# By default, Nginx listens on port 80.
# To modify this, change LISTEN_PORT environment variable.
# (in a Dockerfile or with an option for `docker run`)
ENV LISTEN_PORT 80

# Copy the entrypoint that will generate Nginx additional configs
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Add demo app
COPY ./app /app
WORKDIR /app

CMD ["/usr/bin/supervisord"]
