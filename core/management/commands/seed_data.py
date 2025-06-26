# core/management/commands/seed_data.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from datetime import timedelta
from core.models import Abonnement, Gestionnaire, Specialiste, Client

class Command(BaseCommand):
    help = "Seed initial data: abonnements, gestionnaire, spécialiste"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Créer un gestionnaire s'il n'existe pas
        if not Gestionnaire.objects.exists():
            user_g = User.objects.create_user(
                username="gestionnaire1",
                email="gestionnaire@example.com",
                password="Gestion1234"
            )
            Gestionnaire.objects.create(utilisateur=user_g)
            self.stdout.write(self.style.SUCCESS("✅ Gestionnaire créé."))

        # Créer un spécialiste s'il n'existe pas
        if not Specialiste.objects.exists():
            user_s = User.objects.create_user(
                username="specialiste1",
                email="specialiste@example.com",
                password="Spec1234"
            )
            Specialiste.objects.create(utilisateur=user_s, specialite="Nutritionniste")
            self.stdout.write(self.style.SUCCESS("✅ Spécialiste créé."))

        # Associer les abonnements à un client et un spécialiste existants
        try:
            client = Client.objects.first()
            specialiste = Specialiste.objects.first()

            if client and specialiste:
                abonnements = [
                    {"type": "Basic", "duree": 30},
                    {"type": "Standard", "duree": 90},
                    {"type": "Premium", "duree": 180},
                ]

                for ab in abonnements:
                    _, created = Abonnement.objects.get_or_create(
                        type=ab["type"],
                        client=client,
                        specialiste=specialiste,
                        defaults={
                            "duree": ab["duree"],
                            "date_debut": now(),
                            "date_fin": now() + timedelta(days=ab["duree"]),
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"✅ Abonnement {ab['type']} créé."))
                    else:
                        self.stdout.write(self.style.WARNING(f"⚠️ Abonnement {ab['type']} déjà existant."))

            else:
                self.stdout.write(self.style.ERROR("❌ Impossible de créer les abonnements : client ou spécialiste manquant."))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erreur : {e}"))
