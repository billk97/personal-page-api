FROM python:3.10-alpine
MAINTAINER Vasileios Konstantinou

RUN pip3 install --upgrade pip

ENV PYTHONNUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./page_api /app

RUN adduser -D user
USER user

