FROM python:3.9.4-alpine3.13

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

WORKDIR /app

COPY . /app

