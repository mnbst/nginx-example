#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --http :8000 --workers 2 --master --enable-threads --module app.wsgi

