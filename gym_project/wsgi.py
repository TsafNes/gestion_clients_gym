import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_project.settings')
django.setup()

# ⚙️ Appliquer automatiquement les migrations (utile pour Render)
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"[Migration error] {e}")

# ⚙️ Création automatique du superutilisateur si absent
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(username="nestor.tsafack@yahoo.fr").exists():
        User.objects.create_superuser(
            username="nestor.tsafack@yahoo.fr",
            email="nestor.tsafack@yahoo.fr",
            password="Admin1234"
        )
        print("✅ Superutilisateur créé.")
    else:
        print("ℹ️ Superutilisateur déjà existant.")
except Exception as e:
    print(f"[Superuser creation error] {e}")

# 🚀 Application WSGI
application = get_wsgi_application()
