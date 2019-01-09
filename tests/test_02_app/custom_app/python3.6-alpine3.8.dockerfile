FROM tiangolo/uwsgi-nginx:python3.6-alpine3.8

COPY ./application /application
WORKDIR /application

EXPOSE 8080
