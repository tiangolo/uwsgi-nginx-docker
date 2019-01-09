FROM tiangolo/uwsgi-nginx:python3.6-alpine3.7

COPY ./application /application
WORKDIR /application

EXPOSE 8080
