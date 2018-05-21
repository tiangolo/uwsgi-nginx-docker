FROM python:2.7-alpine3.4

MAINTAINER Sebastian Ramirez <tiangolo@gmail.com>

# Install pip dependencies
RUN apk --no-cache add gcc libc-dev linux-headers pcre pcre-dev py-pip python3-dev

# Install uWSGI
RUN pip install uwsgi

# Standard set up Nginx
ENV NGINX_VERSION 1.12.1-r0

RUN apk --no-cache add nginx ca-certificates
# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log
RUN mkdir /run/nginx
EXPOSE 80 443
# Finished setting up Nginx

# Make NGINX run on the foreground
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# Copy the modified Nginx configs
COPY nginx.conf /etc/nginx/conf.d/
COPY root_nginx.conf /etc/nginx/nginx.conf
# Copy the base uWSGI ini file to enable default dynamic uwsgi process number
COPY uwsgi.ini /etc/uwsgi/

# Install Supervisord
RUN apk --no-cache add supervisor
# Custom Supervisord config
RUN mkdir /etc/supervisor.d
COPY supervisord.conf /etc/supervisor.d/supervisord.ini

# Which uWSGI .ini file should be used, to make it customizable
ENV UWSGI_INI /app/uwsgi.ini

# By default, allow unlimited file sizes, modify it to limit the file sizes
# To have a maximum of 1 MB (Nginx's default) change the line to:
# ENV NGINX_MAX_UPLOAD 1m
ENV NGINX_MAX_UPLOAD 0
RUN sed -i '/client_max_body_size/d' /etc/nginx/nginx.conf

# Copy the entrypoint that will generate Nginx additional configs
RUN apk --no-cache add bash
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Add demo app
COPY ./app /app
WORKDIR /app

CMD ["/usr/bin/supervisord"]
