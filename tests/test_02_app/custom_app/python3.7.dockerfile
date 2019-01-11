FROM tiangolo/uwsgi-nginx:python3.7

COPY ./application /application
WORKDIR /application

EXPOSE 8080
