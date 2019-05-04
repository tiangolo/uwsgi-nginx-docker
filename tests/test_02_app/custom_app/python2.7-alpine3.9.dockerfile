FROM tiangolo/uwsgi-nginx:python2.7-alpine3.9

COPY ./application /application
WORKDIR /application

EXPOSE 8080
