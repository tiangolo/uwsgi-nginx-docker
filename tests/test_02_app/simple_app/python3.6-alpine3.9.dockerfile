FROM tiangolo/uwsgi-nginx:python3.6-alpine3.9

COPY ./app/main.py /app/main.py
