FROM tiangolo/uwsgi-nginx:python3.6

COPY ./application /application
WORKDIR /application

EXPOSE 8080
