#!/bin/sh

pip install --upgrade pip
pip install -r ./requirements.txt


python manage.py collectstatic --no-input
python manage.py migrate

python manage.py shell <<EOF
from django.contrib.auth import get_user_model

User = get_user_model()
username = 'nombre_de_usuario'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, 'correo@example.com', 'contraseña')
EOF


