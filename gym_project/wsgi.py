# gym_project/wsgi.py

import django
from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_project.settings')

application = get_wsgi_application()

# Création automatique du superutilisateur sur Render
from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username="nestor.tsafack@yahoo.fr").exists():
    User.objects.create_superuser(
        username="nestor.tsafack@yahoo.fr",
        email="nestor.tsafack@yahoo.fr",
        password="Admin1234"
    )
