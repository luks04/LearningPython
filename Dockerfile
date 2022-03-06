FROM python:3.9.7-slim-buster

RUN apt update \
    && apt install -y \
    wget \
    nano \
    build-essential \
    python-dev

RUN mkdir /home/main-app
WORKDIR /home/main-app/

COPY main-app/ .

RUN pip install --use-feature=fast-deps --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt
