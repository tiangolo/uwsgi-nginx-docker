#!/bin/bash
set -e

USE_NGINX_UPLOAD=${NGINX_UPLOAD:-0}

echo "client_max_body_size $USE_NGINX_UPLOAD;" > /etc/nginx/conf.d/upload.conf

exec "$@"