FROM python:3.9.7-slim-buster

ADD . /logs_app
WORKDIR /logs_app

RUN apt update \
    && apt install -y \
    wget \
    nano \
    build-essential \
    python-dev

RUN pip install --use-deprecated=legacy-resolver -r requirements.txt
