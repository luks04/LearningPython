FROM python:3.9.7-slim-buster

ADD . /app
WORKDIR /app

RUN pip install uwsgi==2.0.19.1

RUN pip install --use-feature=fast-deps --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt
