FROM python:3.8.0-buster

MAINTAINER = "Leonardo Fiório"

WORKDIR /app

COPY . . 

CMD python app.py
