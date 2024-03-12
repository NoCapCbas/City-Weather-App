#!/bin/sh

echo "Make migrations"
python manage.py makemigrations
echo "Migrate db"
python manage.py migrate --no-input
echo "Collect static files"
python manage.py collectstatic --no-input

# echo "Create django admin"
DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --no-input

echo "Starting server"
gunicorn weather.wsgi:application --bind 0.0.0.0:8000
