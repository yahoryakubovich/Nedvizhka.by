FROM python:3.11

ENV DJANGO_ENV=production

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./README.md /app/README.md
COPY ./nedvizhka /app
COPY ./pyproject.toml /app/pyproject.toml

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
