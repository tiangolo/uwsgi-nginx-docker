FROM tiangolo/uwsgi-nginx:python3.7-alpine3.7

COPY ./app/main.py /app/main.py
