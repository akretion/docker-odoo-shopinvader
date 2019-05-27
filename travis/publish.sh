#!/bin/bash

set -e
IMAGE=quay.io/akretion/shopinvader-odoo

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
  echo "Log to quay.io"
  docker login quay.io --username="$DOCKER_USERNAME" --password="$DOCKER_PASSWORD"
  if [ "$TRAVIS_BRANCH" == "10.0" ]; then
    echo "Publish latest"
    docker tag current-latest $IMAGE:$TRAVIS_BRANCH-latest
    docker push $IMAGE:$TRAVIS_BRANCH-latest
    TAG=$TRAVIS_BRANCH-`date +%Y%m%d-%H%m`
    echo "Publish tagged $TAG"
    docker tag current-latest $IMAGE:$TAG
    docker push $IMAGE:$TAG
  else
    echo "Not pushing any image"
  fi
fi
