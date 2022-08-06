#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py makeusers
python manage.py adddata

gunicorn indicators.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

exec "$@"
