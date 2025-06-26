from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from django.contrib.auth import get_user_model
        from core.models import Abonnement, Gestionnaire, Specialiste
        from django.db.utils import OperationalError, ProgrammingError

        try:
            # Créer les abonnements
            for nom in ['Basic', 'Standard', 'Premium']:
                Abonnement.objects.get_or_create(nom=nom)

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
            # Les tables ne sont peut-être pas encore migrées
            pass
