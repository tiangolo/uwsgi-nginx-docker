FROM tiangolo/uwsgi-nginx:python2.7-alpine3.7

COPY ./application /application
WORKDIR /application

EXPOSE 8080
