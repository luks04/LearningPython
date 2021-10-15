# A Dockerfile specifies how to build a Docker image
FROM python:3

ADD . /app
WORKDIR /app

RUN pip install Flask
RUN pip install Werkzeug
RUN pip install pymongo
RUN pip install flask_sqlalchemy
RUN pip install flask_mail

ENTRYPOINT ["python", "flask_learning/app.py"]