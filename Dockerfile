FROM python:3.9.7-slim-buster

ADD . /app
WORKDIR /app

RUN pip install --use-deprecated=legacy-resolver -r requirements.txt

CMD ["uwsgi", "--ini", "/app/uwsgi_config/uwsgi.ini"]
