## Supported tags and respective `Dockerfile` links

* [`latest`, `python2.7` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-docker/blob/master/python2.7/Dockerfile)
* [`python3.6` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-docker/blob/master/python3.6/Dockerfile)
* [`python3.5` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-docker/blob/master/python3.5/Dockerfile)

# uwsgi-nginx

**Docker** image with **uWSGI** and **Nginx** for **Python 2.7**, **Python 3.5** and **Python 3.6** applications (as **Flask**) in a single container.

## Description

This [**Docker**](https://www.docker.com/) image allows you to create [**Python**](https://www.python.org/) web applications that run with [**uWSGI**](https://uwsgi-docs.readthedocs.org/en/latest/) and [**Nginx**](http://nginx.org/en/) in a single container.

uWSGI with Nginx is one of the best ways to deploy a Python application, so you you should have a [good performance (check the benchmarks)](http://nichol.as/benchmark-of-python-web-servers) with this image.

This image was created to be the base image for [**tiangolo/uwsgi-nginx-flask**](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/) but could be used as the base image to run any Python web application.

If you are creating a new [**Flask**](http://flask.pocoo.org/) web application you should use [**tiangolo/uwsgi-nginx-flask**](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/) instead.

**GitHub repo**: <https://github.com/tiangolo/uwsgi-nginx-docker>

**Docker Hub image**: <https://hub.docker.com/r/tiangolo/uwsgi-nginx/>

## What's new

* 2017-07-31: There's now an image tag for Python 3.6, based on the official image for Python 3.6.

* 2016-10-01: Now you can override default `uwsgi.ini` parameters from the file in `/app/uwsgi.ini`.

* 2016-08-16: There's now an image tag for Python 3.5, based on the official image for Python 3.5. So now you can use this image for your projects in Python 2.7 and Python 3.5.

* 2016-08-16: Use dynamic a number of worker processes for uWSGI, from 2 to 16 depending on load. This should work for most cases. This helps specially when there are some responses that are slow and take time to be generated, this change allows all the other responses to keep fast (in a new process) without having to wait for the first (slow) one to finish.

* Also, it now uses a base `uwsgi.ini` file under `/etc/uwsgi/` with most of the general configurations, so, the `uwsgi.ini` inside `/app` (the one you could need to modify) is now a lot simpler.

* 2016-04-05: Nginx and uWSGI logs are now redirected to stdout, allowing to use `docker logs`.

## How to use

* You shouldn't have to clone the GitHub repo. You should use it as a base image for other images, using `FROM tiangolo/uwsgi-nginx` in your `Dockerfile`.

* Alternatively, you could use `FROM tiangolo/uwsgi-nginx:python2.7`, but this is the default (it is also marked with the `latest` tag), so the result is the same as the method above. Python 2.7 is the default as it is still the most used version of Python and [not necessarily all the packages are available for Python 3.5 or 3.6](http://flask.pocoo.org/docs/0.11/python3/).

If you want to use it as a base image for a Python 3.5 or 3.6 application then you should use `FROM tiangolo/uwsgi-nginx:python3.5` or `FROM tiangolo/uwsgi-nginx:python3.6` in your `Dockerfile`.

If you are building a **Flask** web application you should use instead [**tiangolo/uwsgi-nginx-flask**](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/).

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
