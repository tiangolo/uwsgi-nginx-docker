FROM tiangolo/uwsgi-nginx:python3.7-alpine3.8

COPY ./application /application
COPY ./prestart.sh /app/prestart.sh
WORKDIR /application

EXPOSE 8080
