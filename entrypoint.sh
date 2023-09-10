#!/bin/sh

set -e

# Collect static files
echo Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
echo Apply database migrations
python manage.py migrate

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 900 \
    --log-level=info
