from django.core.management.base import BaseCommand
from core.models import Abonnement, Gestionnaire, Specialiste
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Crée les données initiales : abonnements, gestionnaires, spécialistes"

    def handle(self, *args, **kwargs):
        # 📦 Abonnements
        abonnements = ['Basic', 'Standard', 'Premium']
        for nom in abonnements:
            obj, created = Abonnement.objects.get_or_create(nom=nom)
            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Abonnement créé : {nom}"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ Abonnement existant : {nom}"))

        # 👨‍💼 Gestionnaires
        if not Gestionnaire.objects.exists():
            user = User.objects.create_user(
                username='gestionnaire1',
                email='gestionnaire@example.com',
                password='Gestion1234'
            )
            Gestionnaire.objects.create(utilisateur=user)
            self.stdout.write(self.style.SUCCESS("✅ Gestionnaire ajouté."))
        else:
            self.stdout.write(self.style.WARNING("⚠️ Un gestionnaire existe déjà."))

        # 🧑‍⚕️ Spécialistes
        if not Specialiste.objects.exists():
            user = User.objects.create_user(
                username='specialiste1',
                email='specialiste@example.com',
                password='Spec1234'
            )
            Specialiste.objects.create(utilisateur=user, specialite='Nutritionniste')
            self.stdout.write(self.style.SUCCESS("✅ Spécialiste ajouté."))
        else:
            self.stdout.write(self.style.WARNING("⚠️ Un spécialiste existe déjà."))
