#!/bin/sh

pip install --upgrade pip
pip install -r ./requirements.txt


python manage.py collectstatic --no-input
python manage.py migrate

#echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')" | python manage.py shell
python manage.py loaddata  dev.json


