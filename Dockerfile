# A Dockerfile specifies how to build a Docker image

# Create a ubuntu base image with python 3 installed.
FROM python:3.8

RUN pip install --upgrade pip

RUN adduser -D appnameuser
USER appnameuser
WORKDIR /home/appnameuser

COPY --chown=appnameuser:appnameuser requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

ENV PATH="/home/appnameuser/.local/bin:${PATH}"

COPY --chown=appnameuser:appnameuser . .

# gunicorn <module_name> : <callable_element_name_within_the_application>
CMD gunicorn app:app