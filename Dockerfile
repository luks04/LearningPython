# A Dockerfile specifies how to build a Docker image

# Create a ubuntu base image with python 3 installed.
FROM python:3.8

ADD . /home/app_name
WORKDIR /home/app_name

RUN pip install --upgrade pip
RUN python3 -m venv app_name_env

RUN python -m pip install Flask
RUN python -m pip install gunicorn
RUN python -m pip install Werkzeug
RUN python -m pip install pymongo
RUN python -m pip install flask_sqlalchemy
RUN python -m pip install flask_mail

# gunicorn <module_name> : <callable_element_name_within_the_application>
CMD gunicorn main:main