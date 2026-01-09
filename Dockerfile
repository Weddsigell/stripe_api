FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync

COPY . .

CMD sh -c " \
  uv run manage.py migrate && \
  (uv run manage.py createsuperuser --noinput || true) && \
  uv run manage.py collectstatic --noinput && \
  uv run gunicorn stripe_api.wsgi:application --workers 3 --bind 0.0.0.0:8000 \
"