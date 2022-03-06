# A Dockerfile specifies how to build a Docker image
FROM python:3.7

ADD . /app
WORKDIR /app

RUN python3 -m venv env
RUN pip install --upgrade pip

RUN source env/bin/activate
RUN pip install -r requirements.txt
