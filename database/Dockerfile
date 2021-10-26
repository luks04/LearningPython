# A Dockerfile specifies how to build a Docker image
FROM python:3.7

ADD . /database_app
WORKDIR /database_app

RUN python3 -m venv env
RUN pip install --upgrade pip

RUN pip install Flask
RUN pip install gunicorn

# CMD gunicorn database_app:database_app