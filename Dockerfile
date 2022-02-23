# A Dockerfile specifies how to build a Docker image

# Create a ubuntu base image with python 3 installed.
FROM python:3.8

ADD . /home/app_name
WORKDIR /home/app_name

# Upgrade pip
RUN pip install --upgrade pip

# Creates venv
RUN python3 -m venv app_name_env

# Activate venv
RUN app_name_env/bin/activate

# Install packages inside created venv
RUN python3 -m pip install Flask
RUN python3 -m pip install gunicorn
RUN python3 -m pip install Werkzeug
RUN python3 -m pip install pymongo
RUN python3 -m pip install flask_sqlalchemy
RUN python3 -m pip install flask_mail

# gunicorn <module_name> : <callable_element_name_within_the_application>
CMD gunicorn app:app