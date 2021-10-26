# A Dockerfile specifies how to build a Docker image
FROM python:3.7

ADD . /logs_app
WORKDIR /logs_app

RUN python3 -m venv env
RUN pip install --upgrade pip

RUN pip install Flask
RUN pip install gunicorn

CMD gunicorn logs_app:logs_app