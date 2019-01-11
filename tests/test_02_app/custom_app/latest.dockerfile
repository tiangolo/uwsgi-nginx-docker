FROM tiangolo/uwsgi-nginx:latest

COPY ./application /application
WORKDIR /application

EXPOSE 8080
