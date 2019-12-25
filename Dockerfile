FROM python:3.7-alpine
MAINTAINER umairkhancis

# This won't let the python buffer the output to avoid complexities when running in docker conatiner.
ENV PYTHONUNBUFFERED 1

# install the dependencies.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Seting up the working directory.
# RUN mkdir ./app
WORKDIR /app
COPY ./app /app

# Use a new user to use application to avoid using default root user; for security purposes.
RUN adduser -D appuser
USER appuser