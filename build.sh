#!/bin/sh

RUN pip install --upgrade pip
RUN pip install -r /src/requirements.txt


python manage.py collectstatic --no-input
python manage.py migrate