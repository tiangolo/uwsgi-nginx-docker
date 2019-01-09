import json

from docker.errors import NotFound

CONTAINER_NAME = "uwsgi-nginx-text"


def get_uwsgi_config(container):
    result = container.exec_run(f"uwsgi --show-config")
    return result.output.decode()


def get_nginx_config(container):
    result = container.exec_run(f"/usr/sbin/nginx -T")
    return result.output.decode()


def stop_previous_container(client):
    try:
        previous = client.containers.get(CONTAINER_NAME)
        previous.stop()
        previous.remove()
    except NotFound:
        return None
