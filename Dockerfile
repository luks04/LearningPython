# A Dockerfile specifies how to build a Docker image

# Create a ubuntu base image with python 3 installed.
FROM python:3.8

# Set the working directory
WORKDIR /

# Copy all the files
COPY . .

RUN python3 -m venv env
RUN pip install --upgrade pip

RUN pip install Flask
RUN pip install gunicorn
RUN pip install Werkzeug
RUN pip install pymongo
RUN pip install flask_sqlalchemy
RUN pip install flask_mail

# Expose the required port
EXPOSE 8080

# gunicorn <module_name> : <callable_element_name_within_the_application>
CMD gunicorn main:app