FROM tiangolo/uwsgi-nginx:python3.5

COPY ./application /application
COPY ./prestart.sh /app/prestart.sh
WORKDIR /application

EXPOSE 8080
