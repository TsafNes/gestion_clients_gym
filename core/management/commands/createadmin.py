# core/management/commands/createadmin.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Créer un super utilisateur automatiquement'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username="nestor.tsafack@yahoo.fr").exists():
            User.objects.create_superuser(
                username="nestor.tsafack@yahoo.fr",
                email="nestor.tsafack@yahoo.fr",
                password="Admin1234"
            )
            self.stdout.write(self.style.SUCCESS("✅ Superutilisateur créé !"))
        else:
            self.stdout.write("ℹ️ Utilisateur déjà existant.")
