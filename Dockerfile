# A Dockerfile specifies how to build a Docker image
FROM python:3.7

ADD . /app
WORKDIR /app

RUN python3 -m venv env
RUN pip install --upgrade pip

RUN pip install Flask
RUN pip install gunicorn
RUN pip install requests
RUN pip install rq

# CMD gunicorn app:app