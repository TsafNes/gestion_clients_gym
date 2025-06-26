# gym_project/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_project.settings')

application = get_wsgi_application()

# Ajout : exécuter la commande seed_data une seule fois
try:
    from django.core.management import call_command
    call_command('seed_data')
except Exception as e:
    print(f"Erreur lors du seed : {e}")