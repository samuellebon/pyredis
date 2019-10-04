FROM python:3.7.4-alpine

LABEL maintainer="samuel.lebon@etu.u-pec.fr"
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.name="pyredis"
LABEL org.label-schema.description="Simple python rest api using redis"
LABEL org.label-schema.build-date="2019-10-04T18:41:15Z"
LABEL org.label-schema.docker.cmd="docker run -d -p 5000:5000 pyredis"

COPY . /app

WORKDIR /app

RUN pip3 install --upgrade flask redis

EXPOSE 5000

CMD ["python", "run.py"]