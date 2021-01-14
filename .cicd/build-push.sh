#!/usr/bin/env bash
set -e

for TAG in $(echo $TAGS | jq -r .[]);
do
    IMAGE_NAME="$DOCKERHUB_USERNAME/ng-inx:$TAG"
    docker build -t "$IMAGE_NAME" "./versions/python-buster/$PYTHON_VERSION"
    docker push "$IMAGE_NAME"
done

