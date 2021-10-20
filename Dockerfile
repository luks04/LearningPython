# A Dockerfile specifies how to build a Docker image
FROM python:3.7

ADD flask_learning/ /app
WORKDIR /app

RUN pip install Flask gunicorn
RUN pip install Werkzeug
RUN pip install pymongo
RUN pip install flask_sqlalchemy
RUN pip install flask_mail

# RUN cd flask_learning

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 app:app
# ENTRYPOINT ["python", "flask_learning/app.py"]