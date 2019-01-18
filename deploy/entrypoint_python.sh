#!/usr/bin/env bash

python /var/www/manage.py makemigrations
python /var/www/manage.py migrate
python /var/www/manage.py runserver 0.0.0.0:8000