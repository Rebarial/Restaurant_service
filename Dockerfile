FROM python:latest

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app app

COPY alembic.ini alembic.ini

COPY .env ./app/test.env

ENV PYTHONPATH /src
