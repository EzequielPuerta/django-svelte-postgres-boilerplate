#!/bin/sh
set -e

uv run python manage.py makemigrations --noinput || true
uv run python manage.py migrate --noinput
uv run python manage.py create_groups || true
uv run python manage.py createsuperuser --noinput || true
uv run python manage.py collectstatic --noinput
uv run gunicorn core.wsgi:application --workers 4 --bind 0.0.0.0:8000 --log-level info
