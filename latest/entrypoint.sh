#!/bin/bash
set -e

# Get the maximum upload file size for Nginx, default to 0: unlimited
USE_NGINX_MAX_UPLOAD=${NGINX_MAX_UPLOAD:-0}
# Generate Nginx config for maximum upload file size
echo "client_max_body_size $USE_NGINX_MAX_UPLOAD;" > /etc/nginx/conf.d/upload.conf

echo -e "WARNING: YOU SHOULDN'T BE USING THE 'latest' DOCKER TAG.

The Docker tag 'latest' will be for Python 3.6 soon.

If you need Python 2.7, specify it with:

FROM tiangolo/uwsgi-nginx:python2.7

If you need Python 3.6, specify it with:

FROM tiangolo/uwsgi-nginx:python3.6

Listen to the cow..."

for i in {1..6}
do
   cowsay "WARNING: don't use 'latest', instead use:

FROM tiangolo/uwsgi-nginx:python2.7

or

FROM tiangolo/uwsgi-nginx:python3.6";

   sleep 10;
done

exec "$@"