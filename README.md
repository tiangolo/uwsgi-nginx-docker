## Supported tags and respective `Dockerfile` links

* [`python3.6` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-docker/blob/master/python3.6/Dockerfile)
* [`python3.5` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-docker/blob/master/python3.5/Dockerfile)
* [`python2.7` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-docker/blob/master/python2.7/Dockerfile)
* [`latest` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-docker/blob/master/latest/Dockerfile)

# uwsgi-nginx

**Docker** image with **uWSGI** and **Nginx** for web applications in **Python 3.6**, **Python 3.5** and **Python 2.7** (as **Flask**) in a single container.

## NOTICE

Soon the tag `latest` will point to `python3.6` instead of `python2.7`.

If you are using in your `Dockerfile`:

```Dockerfile
FROM tiangolo/uwsgi-nginx:latest
```

you should update it to:

```Dockerfile
FROM tiangolo/uwsgi-nginx:python2.7
```

## Description

This [**Docker**](https://www.docker.com/) image allows you to create [**Python**](https://www.python.org/) web applications that run with [**uWSGI**](https://uwsgi-docs.readthedocs.org/en/latest/) and [**Nginx**](http://nginx.org/en/) in a single container.

uWSGI with Nginx is one of the best ways to deploy a Python application, so you should have a [good performance (check the benchmarks)](http://nichol.as/benchmark-of-python-web-servers) with this image.

This image was created to be the base image for [**tiangolo/uwsgi-nginx-flask**](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/) but could be used as the base image to run any Python web application.

If you are creating a new [**Flask**](http://flask.pocoo.org/) web application you should use [**tiangolo/uwsgi-nginx-flask**](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/) instead.

**GitHub repo**: <https://github.com/tiangolo/uwsgi-nginx-docker>

**Docker Hub image**: <https://hub.docker.com/r/tiangolo/uwsgi-nginx/>

## How to use

* You shouldn't have to clone the GitHub repo. You should use it as a base image for other images, using this in your `Dockerfile`:

```Dockerfile
FROM tiangolo/uwsgi-nginx:python3.6

# Your Dockerfile code...
```

* But, if you need Python 2.7 that line would have to be `FROM tiangolo/uwsgi-nginx:python2.7`.

* By default it will try to find a uWSGI config file in `/app/uwsgi.ini`.

* That `uwsgi.ini` file will make it try to run a Python file in `/app/main.py`.

If you are building a **Flask** web application you should use instead [**tiangolo/uwsgi-nginx-flask**](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/).

## Advanced usage

### Custom app directory

If you need to use a directory for your app different than `/app`, you can override the uWSGI config file path with an environment variable `UWSGI_INI`, and put your custom `uwsgi.ini` file there. 

For example, if you needed to have your application directory in `/application` instead of `/app`, your `Dockerfile` would look like:

```Dockerfile
FROM tiangolo/uwsgi-nginx:python3.6

ENV UWSGI_INI /application/uwsgi.ini

COPY ./application /application
WORKDIR /appapplication
```

And your `uwsgi.ini` file in `./application/uwsgi.ini` would contain:

```ini
[uwsgi]
wsgi-file=/application/main.py
```

**Note**: it's important to include the `WORKDIR` option, otherwise uWSGI will start the application in `/app`.

### Custom max upload size

In this image, Nginx is configured to allow unlimited upload file sizes. This is done because by default a simple Python server would allow that, so that's the simplest behavior a developer would expect.

If you need to restrict the maximum upload size in Nginx, you can add an environment variable `NGINX_MAX_UPLOAD` and assign a value corresponding to the [standard Nginx config `client_max_body_size`](http://nginx.org/en/docs/http/ngx_http_core_module.html#client_max_body_size).

For example, if you wanted to set the maximum upload file size to 1 MB (the default in a normal Nginx installation), you would need to set the `NGINX_MAX_UPLOAD` environment variable to the value `1m`. Then the image would take care of adding the corresponding configuration file (this is done by the `entrypoint.sh`).

So, your `Dockerfile` would look something like:

```Dockerfile
FROM tiangolo/uwsgi-nginx:python3.6

ENV NGINX_MAX_UPLOAD 1m

COPY ./app /app
```

### Custom listen port

By default, the container made from this image will listen on port 80.

To change this behavior, set the `LISTEN_PORT` environment variable.

You can do that in your `Dockerfile`, it would look something like:

```Dockerfile
FROM tiangolo/uwsgi-nginx:python3.6

ENV LISTEN_PORT 8080

COPY ./app /app
```

## What's new

* 2017-12-08: Now you can configure which port the container should listen on, using the environment variable `LISTEN_PORT`.

* 2017-08-09: You can set a custom maximum upload file size using an environment variable `NGINX_MAX_UPLOAD`, by default it has a value of `0`, that allows unlimited upload file sizes. This differs from Nginx's default value of 1 MB. It's configured this way because that's the simplest experience a developer that is not expert in Nginx would expect.

* 2017-08-09: Now you can override where to look for the `uwsgi.ini` file, and with that, change the default directory from `/app` to something else, using the envirnoment variable `UWSGI_INI`.

* 2017-08-08: There's a new `latest` tag image, just to show a warning for those still using `latest` for Python 2.7 web applications. As of now, [everyone](https://www.python.org/dev/peps/pep-0373/) [should be](http://flask.pocoo.org/docs/0.12/python3/#python3-support) [using Python 3](https://docs.djangoproject.com/en/1.11/faq/install/#what-python-version-should-i-use-with-django).

* 2017-08-08: Supervisord now terminates uWSGI on `SIGTERM`, so if you run `docker stop` or something similar, it will actually stop everything, instead of waiting for Docker's timeout to kill the container.

* 2017-07-31: There's now an image tag for Python 3.6, based on the official image for Python 3.6.

* 2016-10-01: Now you can override default `uwsgi.ini` parameters from the file in `/app/uwsgi.ini`.

* 2016-08-16: There's now an image tag for Python 3.5, based on the official image for Python 3.5. So now you can use this image for your projects in Python 2.7 and Python 3.5.

* 2016-08-16: Use dynamic a number of worker processes for uWSGI, from 2 to 16 depending on load. This should work for most cases. This helps especially when there are some responses that are slow and take some time to be generated, this change allows all the other responses to keep fast (in a new process) without having to wait for the first (slow) one to finish.

* Also, it now uses a base `uwsgi.ini` file under `/etc/uwsgi/` with most of the general configurations, so, the `uwsgi.ini` inside `/app` (the one you could need to modify) is now a lot simpler.

* 2016-04-05: Nginx and uWSGI logs are now redirected to stdout, allowing to use `docker logs`.

## Technical details

One of the best ways to deploy a Python web application is with uWSGI and Nginx, as seen in the [benchmarks](http://nichol.as/benchmark-of-python-web-servers).

Roughly:

* **Nginx** is a web server, it takes care of the HTTP connections and also can serve static files directly and more efficiently.

* **uWSGI** is an application server, that's what runs your Python code and it talks with Nginx.

* **Your Python code** has the actual web application, and is run by uWSGI.

This image takes advantage of already slim and optimized existing Docker images (based on Debian as [recommended by Docker](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)) and implements Docker best practices.

It uses the official Python Docker image, installs uWSGI and on top of that, with the least amount of modifications, adds the official Nginx image (as of 2016-02-14).

And it controls all these processes with Supervisord.

---

There's the rule of thumb that you should have "one process per container".

That helps, for example, isolating an app and its database in different containers.

But if you want to have a "micro-services" approach you may want to [have more than one process in one container](https://valdhaus.co/writings/docker-misconceptions/) if they are all related to the same "service", and you may want to include your Flask code, uWSGI and Nginx in the same container (and maybe run another container with your database).

That's the approach taken in this image.

---

This image has a default sample "Hello World" app in the container's `/app` directory using the example in the [uWSGI documentation](http://uwsgi-docs.readthedocs.org/en/latest/WSGIquickstart.html).

You probably want to override it or delete it in your project.

It is there in case you run this image by itself and not as a base image for your own `Dockerfile`, so that you get a sample app without errors.

## License

This project is licensed under the terms of the Apache license.
