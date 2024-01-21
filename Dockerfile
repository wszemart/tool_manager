FROM python:3.9

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY pyproject.toml /app

COPY poetry.lock /app

COPY . .

RUN pip3 install poetry

RUN poetry install
