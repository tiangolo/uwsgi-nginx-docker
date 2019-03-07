#!/bin/bash

# This script will generate the Dockerfiles
set -e

cd $(dirname "$0")/..

function generate {
    VERSION="$1"
    DESTINATION_NAME="$2"
    mkdir -p "$DESTINATION_NAME"
    cp -r templates/files/* "$DESTINATION_NAME"
    sed -e "s/python3.7/python$VERSION/g" -i "$DESTINATION_NAME/entrypoint.sh"
}

function generate_debian {
    VERSION=$1
    DESTINATION_NAME="python$VERSION"
    generate "$VERSION" "$DESTINATION_NAME"
    sed -e 's/\$DOCKER_PYTHON_VERSION/'"$VERSION"'/g' "templates/Dockerfile-debian" > "$DESTINATION_NAME/Dockerfile"
}

function generate_alpine {
    VERSION=$1
    ALPINE_VERSION=$2
    DESTINATION_NAME="python$VERSION-alpine$ALPINE_VERSION"
    generate "$VERSION" "$DESTINATION_NAME"
    sed -e 's/\$DOCKER_PYTHON_VERSION/'"$VERSION"'/g' "templates/Dockerfile-alpine" > "$DESTINATION_NAME/Dockerfile"
    sed -e 's/\$DOCKER_ALPINE_VERSION/'"$ALPINE_VERSION"'/g' -i "$DESTINATION_NAME/Dockerfile"
    echo "plugin = python3" >> "$DESTINATION_NAME/uwsgi.ini"
}

for VERSION in 3.5 3.6 3.7; do
    generate_debian $VERSION
    for ALPINE_VERSION in 3.7 3.8; do
        generate_alpine $VERSION $ALPINE_VERSION
    done
done

# Python 2.7 is special in some cases, handle it manually
for VERSION in 2.7; do
    generate_debian $VERSION
    for ALPINE_VERSION in 3.7 3.8; do
        generate_alpine $VERSION $ALPINE_VERSION
        sed -e 's/uwsgi-python3/uwsgi-python/g' -i "python$VERSION-alpine$ALPINE_VERSION/Dockerfile"
        sed -e 's/python3/python/g' -i "python$VERSION-alpine$ALPINE_VERSION/uwsgi.ini"
    done
done
