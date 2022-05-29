#!/bin/bash

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :8000 --master --module app.wsgi --processes 4 --threads 2 --thunder-lock

