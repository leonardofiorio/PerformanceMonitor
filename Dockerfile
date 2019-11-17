FROM python:3.8.0

MAINTAINER = "Leonardo Fiório"

WORKDIR /app

COPY . . 

RUN pip install requests				

CMD python -u app.py
