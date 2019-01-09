import time

import docker
import pytest
import requests
from requests import Response

from ..utils import CONTAINER_NAME, stop_previous_container, get_uwsgi_config, get_nginx_config

client = docker.from_env()


@pytest.mark.parametrize(
    "image,response_text",
    [
        (
            "tiangolo/uwsgi-nginx:python2.7",
            "Hello World from a default Nginx uWSGI Python 2.7 app in a Docker container (default)",
        ),
        (
            "tiangolo/uwsgi-nginx:python2.7-alpine3.7",
            "Hello World from a default Nginx uWSGI Python 2.7 app in a Docker container in Alpine (default)",
        ),
        (
            "tiangolo/uwsgi-nginx:python2.7-alpine3.8",
            "Hello World from a default Nginx uWSGI Python 2.7 app in a Docker container in Alpine (default)",
        ),
        (
            "tiangolo/uwsgi-nginx:python3.5",
            "Hello World from a default Nginx uWSGI Python 3.5 app in a Docker container (default)",
        ),
        (
            "tiangolo/uwsgi-nginx:python3.6",
            "Hello World from a default Nginx uWSGI Python 3.6 app in a Docker container (default)",
        ),
        (
            "tiangolo/uwsgi-nginx:python3.6-alpine3.7",
            "Hello World from a default Nginx uWSGI Python 3.6 app in a Docker container in Alpine (default)",
        ),
        (
            "tiangolo/uwsgi-nginx:python3.6-alpine3.8",
            "Hello World from a default Nginx uWSGI Python 3.6 app in a Docker container in Alpine (default)",
        ),
        (
            "tiangolo/uwsgi-nginx:python3.7",
            "Hello World from a default Nginx uWSGI Python 3.7 app in a Docker container (default)",
        ),
        # (
        #     "tiangolo/uwsgi-nginx:python3.7-alpine3.7",
        #     "Hello World from a default Nginx uWSGI Python 3.7 app in a Docker container in Alpine (default)",
        # ),
        # (
        #     "tiangolo/uwsgi-nginx:python3.7-alpine3.8",
        #     "Hello World from a default Nginx uWSGI Python 3.7 app in a Docker container in Alpine (default)",
        # ),
    ],
)
def test_defaults(image, response_text):
    stop_previous_container(client)
    container = client.containers.run(
        image, name=CONTAINER_NAME, ports={"80": "8000"}, detach=True
    )
    uwsgi_config = get_uwsgi_config(container)
    assert "ini = /app/uwsgi.ini" in uwsgi_config
    assert "wsgi-file = /app/main.py" in uwsgi_config
    assert "processes = 16" in uwsgi_config
    assert "cheaper = 2" in uwsgi_config
    nginx_config = get_nginx_config(container)
    assert "client_max_body_size 0;" in nginx_config
    assert "worker_processes 1;" in nginx_config
    assert "listen 80;" in nginx_config
    time.sleep(5)
    response: Response = requests.get("http://127.0.0.1:8000")
    assert response.status_code == 200
    assert response.text == response_text
    container.stop()
    container.remove()
