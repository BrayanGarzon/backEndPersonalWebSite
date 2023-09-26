#!/bin/sh

pip install --upgrade pip
pip install -r /src/requirements.txt


python manage.py collectstatic --no-input
python manage.py migrate