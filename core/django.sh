#!/bin/bash

echo 'Makemigratons step'
python manage.py makemigrations
echo '--------------------------'

echo 'Migrate step'
python manage.py migrate
echo '--------------------------'

echo 'Runserver step'
python manage.py runserver
echo '--------------------------'