FROM tiangolo/uwsgi-nginx:python3.5

COPY ./application /application
WORKDIR /application

EXPOSE 8080
