#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/Users/danil/Documents/Study/2_CURSOS_ONLINE/profiles-rest-api'

git pull
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput
supervisorctl restart profiles_api

echo "DONE! :)"
