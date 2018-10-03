FROM ubuntu:latest
LABEL Abdul Rehman

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

#Add source files
COPY . /app
ENV HOME=/app

WORKDIR /app
RUN pip install -r requirements.txt

ENV FLASK_APP=python-ary-app.py

EXPOSE 5000

ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "wsgi:app" ]


