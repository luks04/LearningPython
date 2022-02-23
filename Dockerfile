# A Dockerfile specifies how to build a Docker image

# Create a ubuntu base image with python 3 installed.
FROM heroku/miniconda

ADD . /home/app_name
WORKDIR /home/app_name

# Creates venv
RUN conda env create -n app_name_env

# Activate venv
RUN conda activate app_name_env

# Install packages inside created venv
RUN conda install Flask
RUN conda install gunicorn
RUN conda install Werkzeug
RUN conda install pymongo
RUN conda install flask_sqlalchemy
RUN conda install flask_mail

# gunicorn <module_name> : <callable_element_name_within_the_application>
CMD gunicorn app:app