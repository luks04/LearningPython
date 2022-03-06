FROM python:3.9.7-slim-buster

RUN pip install uwsgi

ADD . /app
WORKDIR /app

RUN pip install --use-deprecated=legacy-resolver -r requirements.txt

CMD ["uwsgi", "--ini", "/app/uwsgi_config/uwsgi.ini"]
