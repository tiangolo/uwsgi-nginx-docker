FROM tiangolo/uwsgi-nginx:python3.7-alpine3.8

COPY ./application /application
WORKDIR /application

EXPOSE 8080
