import os
import subprocess
import sys

versions = [
    {
        "NAME": "python2.7",
        "BUILD_PATH": "python2.7",
        "TEST_STR1": "Hello World from a default Nginx uWSGI Python 2.7 app in a Docker container (default)",
        "DOCKERFILE": "python2.7.dockerfile",
        "TEST_STR2": "Hello World from Nginx uWSGI Python 2.7 app in a Docker container",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python2.7-alpine3.7",
        "BUILD_PATH": "python2.7-alpine3.7",
        "TEST_STR1": "Hello World from a default Nginx uWSGI Python 2.7 app in a Docker container in Alpine (default)",
        "DOCKERFILE": "python2.7-alpine3.7.dockerfile",
        "TEST_STR2": "Hello World from Nginx uWSGI Python 2.7 app in a Docker container",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python2.7-alpine3.8",
        "BUILD_PATH": "python2.7-alpine3.8",
        "TEST_STR1": "Hello World from a default Nginx uWSGI Python 2.7 app in a Docker container in Alpine (default)",
        "DOCKERFILE": "python2.7-alpine3.8.dockerfile",
        "TEST_STR2": "Hello World from Nginx uWSGI Python 2.7 app in a Docker container",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python3.5",
        "BUILD_PATH": "python3.5",
        "TEST_STR1": "Hello World from a default Nginx uWSGI Python 3.5 app in a Docker container (default)",
        "DOCKERFILE": "python3.5.dockerfile",
        "TEST_STR2": "Hello World from Nginx uWSGI Python 3.5 app in a Docker container",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python3.6",
        "BUILD_PATH": "python3.6",
        "TEST_STR1": "Hello World from a default Nginx uWSGI Python 3.6 app in a Docker container (default)",
        "DOCKERFILE": "python3.6.dockerfile",
        "TEST_STR2": "Hello World from Nginx uWSGI Python 3.6 app in a Docker container",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python3.6-alpine3.7",
        "BUILD_PATH": "python3.6-alpine3.7",
        "TEST_STR1": "Hello World from a default Nginx uWSGI Python 3.6 app in a Docker container in Alpine (default)",
        "DOCKERFILE": "python3.6-alpine3.7.dockerfile",
        "TEST_STR2": "Hello World from Nginx uWSGI Python 3.6 app in a Docker container",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python3.6-alpine3.8",
        "BUILD_PATH": "python3.6-alpine3.8",
        "TEST_STR1": "Hello World from a default Nginx uWSGI Python 3.6 app in a Docker container in Alpine (default)",
        "DOCKERFILE": "python3.6-alpine3.8.dockerfile",
        "TEST_STR2": "Hello World from Nginx uWSGI Python 3.6 app in a Docker container",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python3.7",
        "BUILD_PATH": "python3.7",
        "TEST_STR1": "Hello World from a default Nginx uWSGI Python 3.7 app in a Docker container (default)",
        "DOCKERFILE": "python3.7.dockerfile",
        "TEST_STR2": "Hello World from Nginx uWSGI Python 3.7 app in a Docker container",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "latest",
        "BUILD_PATH": "python3.7",
        "TEST_STR1": "Hello World from a default Nginx uWSGI Python 3.7 app in a Docker container (default)",
        "DOCKERFILE": "latest.dockerfile",
        "TEST_STR2": "Hello World from Nginx uWSGI Python 3.7 app in a Docker container",
        "RUN_TESTS": "1",
    },
    {
        "NAME": "python3.7-alpine3.7",
        "BUILD_PATH": "python3.7-alpine3.7",
        "TEST_STR1": "Hello World from a default Nginx uWSGI Python 3.7 app in a Docker container in Alpine (default)",
        "DOCKERFILE": "python3.7-alpine3.7.dockerfile",
        "TEST_STR2": "Hello World from Nginx uWSGI Python 3.7 app in a Docker container",
        "RUN_TESTS": "",
    },
    {
        "NAME": "python3.7-alpine3.8",
        "BUILD_PATH": "python3.7-alpine3.8",
        "TEST_STR1": "Hello World from a default Nginx uWSGI Python 3.7 app in a Docker container in Alpine (default)",
        "DOCKERFILE": "python3.7-alpine3.8.dockerfile",
        "TEST_STR2": "Hello World from Nginx uWSGI Python 3.7 app in a Docker container",
        "RUN_TESTS": "",
    },
]


def test_tag(*, env: dict):
    use_env = {**os.environ, **env}
    return_code = subprocess.call(["bash", "scripts/test.sh"], env=use_env)
    if return_code != 0:
        sys.exit(return_code)


def print_version_envs():
    env_lines = []
    for version in versions:
        env_vars = []
        for key, value in version.items():
            env_vars.append(f"{key}='{value}'")
        env_lines.append(" ".join(env_vars))
    for line in env_lines:
        print(line)


def main():
    for env in versions:
        test_tag(env=env)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print_version_envs()
    else:
        main()
