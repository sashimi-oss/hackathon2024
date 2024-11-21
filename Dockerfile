# pythonのバージョンは任意
FROM python:3.9

WORKDIR /app
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN echo "deb http://archive.debian.org/debian/ stretch main" > /etc/apt/sources.list \
    && echo "deb http://archive.debian.org/debian-security stretch/updates main" >> /etc/apt/sources.list 
#      ↑ 実行すると  apt update　→　apt install vim などができる
RUN apt-get update 

ENV LC_ALL ja_JP.UTF-8