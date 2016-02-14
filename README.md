# uwsgi-nginx

**Docker** image with **uWSGI** and **Nginx** for **Python** applications (in a
single container).

## Description

The image allows you to create **Python** applications that run
with **uWSGI** and **Nginx**.

There are also two specialized **Flask** images (tags).

uWSGI with Nginx is one of the best ways to deploy a Python
application, so you know you'll have a good performance.

## In a hurry?

* Go to `example-flask` (in this repository)
* Copy that directory as a template for your Flask application
* Adapt it to your needs
* Build your Docker container with:

```
docker build -t my-flask-app .
```

* Run your Docker container with:

```
docker run -d --name my-flask-app -p 80:80 my-flask-app
```

...and you have an optimized Flask server in a Docker container.

## Building an Angular JS app (or similar) with Flask?

Do the same as "**In a hurry?**" (above) but with the directory `example-flask-index`.


## Usage

You don't have to clone this repo, you should be able to use one
of the images as a base image for your Dockerfiles.

There are 3 Docker images:

* **[base](base)**: A bare bones image including uWSGI, Nginx and a
very simple sample Hello World application. You probably don't
want to use this image directly but instead one of the Flask
images.

* **[flask](flask)**: An image based on the **base** image, including
Flask and a sample template app. You probably want to use this
as your base image.

* **[flask-index](flask-index)**: An image based on the **flask** image, but
optimizing the configuration to make Nginx serve
`/app/static/index.html` directly when requested for `/`. This is
specially helpful (and efficient) if you are building a
single-page app without templates (as with Angular JS) and using
Flask as an API / back-end.

You may want to go to the directory of the base image that applies
the most to you and read it's README: **[base](base)**, **[flask](flask)**,
**[flask-index](flask-index)**.

You may also want to start a Flask app using one of the example templates:
**[example-flask](example-flask)** or **[example-flask-index](example-flask-index)**.

## Technical details

One of the best ways to deploy a Python application is with uWSGI
and Nginx, as seen in the
[benchmarks](http://nichol.as/benchmark-of-python-web-servers).

Roughly:

* **Nginx** is a web server, it takes care of the HTTP connections and
also can serve static files directly and more efficiently.

* **uWSGI** is an application server, that's what runs your Python
code.

* **Your Python code** has the actual application, and is run by
uWSGI.

These images take advantage of already slim and optimized
existing Docker images, implementing best practices. They use
the official Python Docker image, install uWSGI and on top of
that, with the least amount of modifications, add the official
Nginx image (as of 2016-02-14).

There's the rule of thumb that you should have "one process per
container". That helps, for example, isolating an app from its
database in different containers. But if you want to have a
"micro-services" approach you may want to [have more than one
process in one container](https://valdhaus.co/writings/docker-misconceptions/) if they are all related to the
same "service", and you may want to include your code, uWSGI
and Nginx in the same container (and maybe run another container
with your database). That's the approach taken in this image.

## License

This project is licensed under the terms of the Apache license.