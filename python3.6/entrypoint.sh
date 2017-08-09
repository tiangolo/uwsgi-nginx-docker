#!/bin/bash
set -e

USE_NGINX_MAX_UPLOAD=${NGINX_MAX_UPLOAD:-0}

echo "client_max_body_size $USE_NGINX_MAX_UPLOAD;" > /etc/nginx/conf.d/upload.conf

exec "$@"