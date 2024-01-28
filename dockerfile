FROM python:3.11-slim-buster

RUN pip install poetry==1.7.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=0 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./

COPY src ./src

RUN poetry install --without dev --no-root

ENTRYPOINT ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "--app-dir", "./src/", "api:app"]
