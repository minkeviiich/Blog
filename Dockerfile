FROM python:3.10.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install "poetry>=1.7.1"
RUN poetry config virtualenvs.create false --local
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-root

COPY testsite .
