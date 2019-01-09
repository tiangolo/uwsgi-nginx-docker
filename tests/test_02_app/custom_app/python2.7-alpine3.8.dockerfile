FROM tiangolo/uwsgi-nginx:python2.7-alpine3.8

COPY ./application /application
WORKDIR /application

EXPOSE 8080
