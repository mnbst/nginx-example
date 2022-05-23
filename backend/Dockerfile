FROM python:3.10.4-slim-buster
LABEL maintainer="awsdevelopper.com"
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
COPY /src /src
COPY requirements.txt /src/

RUN apt-get -y update &&\
    apt-get -y upgrade &&\
     apt-get -y install libpq-dev gcc &&\
     apt-get check &&\
     apt-get clean

RUN python -m venv /py &&\
    /py/bin/pip install --upgrade pip &&\
    /py/bin/pip install -r /src/requirements.txt &&\
    adduser --disabled-password --no-create-home app

ENV PATH="/py/bin:$PATH"

USER app
