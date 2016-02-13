FROM tiangolo/uwsgi-nginx

MAINTAINER Sebastian Ramirez <tiangolo@gmail.com>

RUN pip install flask

# Remove default configuration from Nginx
RUN rm /etc/nginx/conf.d/default.conf
# Add app configuration to Nginx
COPY nginx.conf /etc/nginx/conf.d/
# Copy sample app
COPY ./app /app



# CMD ["nginx", "-g", "daemon off;"]
