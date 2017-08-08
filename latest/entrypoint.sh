#!/bin/bash
set -e

echo -e "WARNING: YOU SHOULDN'T BE USING THE 'latest' DOCKER TAG.

The Docker tag 'latest' will be for Python 3.6 soon.

If you need Python 2.7, specify it with:

FROM tiangolo/uwsgi-nginx:python2.7

If you need Python 3.6, specify it with:

FROM tiangolo/uwsgi-nginx:python3.6

Listen to the cow..."

for i in {1..3}
do
   cowsay "WARNING: don't use 'latest', instead use:

FROM tiangolo/uwsgi-nginx:python2.7

or

FROM tiangolo/uwsgi-nginx:python3.6";

   sleep 10;
done

exec "$@"