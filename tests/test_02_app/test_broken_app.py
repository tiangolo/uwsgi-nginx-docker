import os
import time
from pathlib import Path

import docker
from docker.models.containers import Container

from ..utils import (
    CONTAINER_NAME,
    generate_dockerfile_content_simple_app,
    get_logs,
    remove_previous_container,
)

client = docker.from_env()


def verify_container(container: Container) -> None:
    logs = get_logs(container)
    assert 'unable to find "application" callable in file /app/main.py' in logs
    assert (
        "unable to load app 0 (mountpoint='') (callable not found or import error)"
        in logs
    )
    assert "*** no app loaded. GAME OVER ***" in logs
    assert "INFO exited: uwsgi (exit status 22; not expected)" in logs
    assert (
        "INFO success: quit_on_failure entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)"
        in logs
    )
    assert "WARN received SIGTERM indicating exit request" in logs
    assert "INFO stopped: nginx (exit status 0)" in logs
    assert "INFO stopped: quit_on_failure (terminated by SIGTERM)" in logs


def test_on_broken_quit_container() -> None:
    name = os.getenv("NAME", "")
    dockerfile_content = generate_dockerfile_content_simple_app(name)
    dockerfile = "Dockerfile"
    sleep_time = int(os.getenv("SLEEP_TIME", 3))
    remove_previous_container(client)
    tag = "uwsgi-nginx-testimage"
    test_path = Path(__file__)
    path = test_path.parent / "broken_app"
    dockerfile_path = path / dockerfile
    dockerfile_path.write_text(dockerfile_content)
    client.images.build(path=str(path), dockerfile=dockerfile, tag=tag)
    container: Container = client.containers.run(
        tag, name=CONTAINER_NAME, ports={"80": "8000"}, detach=True
    )
    time.sleep(sleep_time)
    verify_container(container)
    updated_container: Container = client.containers.get(container.id)
    assert updated_container.status == "exited"
    container.stop()
