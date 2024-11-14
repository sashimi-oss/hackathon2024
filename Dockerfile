# pythonのバージョンは任意
FROM python:3.9

WORKDIR /app
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update 

ENV LC_ALL ja_JP.UTF-8