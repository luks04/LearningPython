# A Dockerfile specifies how to build a Docker image

# Create a ubuntu base image with python 3 installed.
FROM python:3.8

ADD . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN python3 -m venv app_name_env

RUN pip install requirements.txt

# gunicorn <module_name> : <callable_element_name_within_the_application>
CMD gunicorn app:app