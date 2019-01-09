FROM tiangolo/uwsgi-nginx:python3.6-alpine3.8

COPY ./app/main.py /app/main.py
