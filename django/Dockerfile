FROM python:3.10.4-slim-buster
LABEL maintainer="awsdevelopper.com"
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
COPY requirements.txt /code/
RUN apt-get -y update && apt-get -y install libpq-dev gcc
RUN python -m venv /py &&\
    /py/bin/pip install --upgrade pip &&\
    /py/bin/pip install -r /code/requirements.txt &&\
    adduser --disabled-password --no-create-home app

ENV PATH="/py/bin:$PATH"

USER app