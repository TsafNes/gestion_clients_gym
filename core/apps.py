from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from django.contrib.auth import get_user_model
        from core.models import Abonnement, Gestionnaire, Specialiste
        from django.utils.timezone import now
        from datetime import timedelta
        from django.db.utils import OperationalError, ProgrammingError

        try:
            # Créer les abonnements
            abonnements = [
                {"type": "Basic", "duree": 30},
                {"type": "Standard", "duree": 90},
                {"type": "Premium", "duree": 180},
            ]
            for ab in abonnements:
                Abonnement.objects.get_or_create(
                    type=ab["type"],
                    defaults={
                        "duree": ab["duree"],
                        "date_debut": now(),
                        "date_fin": now() + timedelta(days=ab["duree"]),
                        "client_id": 1,         # Remplacer avec un ID existant
                        "specialiste_id": 1     # Idem
                    }
                )

            # Créer un gestionnaire si aucun n'existe
            User = get_user_model()
            if not Gestionnaire.objects.exists():
                user_g = User.objects.create_user(
                    username='gestionnaire1',
                    email='gestionnaire@example.com',
                    password='Gestion1234'
                )
                Gestionnaire.objects.create(utilisateur=user_g)

            # Créer un spécialiste si aucun n'existe
            if not Specialiste.objects.exists():
                user_s = User.objects.create_user(
                    username='specialiste1',
                    email='specialiste@example.com',
                    password='Spec1234'
                )
                Specialiste.objects.create(utilisateur=user_s, specialite='Nutritionniste')

        except (OperationalError, ProgrammingError):
            pass  # Les tables ne sont peut-être pas encore prêtes
