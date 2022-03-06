FROM python:3.9.7-slim-buster

ADD . /app
WORKDIR /app

RUN apt update \
    && apt install -y \
    wget \
    nano \
    build-essential \
    python-dev

RUN pip install --use-feature=fast-deps --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt
