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
            User = get_user_model()

            # 🟣 Créer les abonnements sans client/spécialiste pour éviter les erreurs FK
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
                    }
                )

            # 🟣 Créer ou réinitialiser le gestionnaire
            if User.objects.filter(username="gestionnaire1").exists():
                user_g = User.objects.get(username="gestionnaire1")
                user_g.set_password("Gestion1234!")
                user_g.save()
            else:
                user_g = User.objects.create_user(
                    username='gestionnaire1',
                    email='gestionnaire@example.com',
                    password='Gestion1234!'
                )
                Gestionnaire.objects.create(utilisateur=user_g)

            # 🟣 Créer ou réinitialiser le spécialiste
            if User.objects.filter(username="specialiste1").exists():
                user_s = User.objects.get(username="specialiste1")
                user_s.set_password("Spec1234!")
                user_s.save()
            else:
                user_s = User.objects.create_user(
                    username='specialiste1',
                    email='specialiste@example.com',
                    password='Spec1234!'
                )
                Specialiste.objects.create(utilisateur=user_s, specialite='Nutritionniste')

            # 🟣 Créer ou réinitialiser le superutilisateur
            admin_username = "nestor.tsafack@yahoo.fr"
            if User.objects.filter(username=admin_username).exists():
                admin = User.objects.get(username=admin_username)
                admin.set_password("Admin1234!")
                admin.save()
            else:
                User.objects.create_superuser(
                    username=admin_username,
                    email=admin_username,
                    password="Admin1234!"
                )

        except (OperationalError, ProgrammingError):
            pass  # La base n’est pas encore migrée
