from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from datetime import timedelta
from django.utils import timezone
from core.models import CustomUser, Abonnement, Client, Gestionnaire, Notification, RendezVous

class AuthenticatedTestCase(APITestCase):
    def authenticate(self, role="gestionnaire"):
        self.user = CustomUser.objects.create_user(username="testuser", password="pass", role=role)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

class AbonnementViewTests(AuthenticatedTestCase):
    def setUp(self):
        self.authenticate(role="gestionnaire")
        self.url = reverse('abonnement-list')

    def test_create_abonnement(self):
        data = {
            "type": "Mensuel",
            "duree": 30,
            "date_debut": timezone.now().date(),
            "date_fin": (timezone.now() + timedelta(days=30)).date()
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ClientViewTests(AuthenticatedTestCase):
    def setUp(self):
        self.authenticate(role="gestionnaire")
        self.gestionnaire = Gestionnaire.objects.create(
            nom="Doe", prenom="Jane", identifiant="g1", mot_de_passe="pw"
        )
        self.abonnement = Abonnement.objects.create(
            type="Test", duree=10,
            date_debut=timezone.now().date(),
            date_fin=(timezone.now() + timedelta(days=10)).date()
        )
        self.url = reverse('client-list')

    def test_create_client(self):
        data = {
            "nom": "Test",
            "prenom": "Client",
            "telephone": "123456",
            "courriel": "client@example.com",
            "nb_heures_restantes": 10,
            "abonnement": self.abonnement.id,
            "gestionnaire": self.gestionnaire.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class GestionnaireViewTests(AuthenticatedTestCase):
    def setUp(self):
        self.authenticate(role="gestionnaire")
        self.url = reverse('gestionnaire-list')

    def test_create_gestionnaire(self):
        data = {
            "nom": "Smith",
            "prenom": "John",
            "identifiant": "jsmith",
            "mot_de_passe": "secure"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class RendezVousViewTests(AuthenticatedTestCase):
    def setUp(self):
        self.authenticate(role="specialiste")
        self.client_user = CustomUser.objects.create_user(username="clientuser", password="pass", role="client")
        self.url = reverse('rendezvous-list')

    def test_create_rendezvous(self):
        data = {
            "client": self.client_user.id,
            "specialiste": self.user.id,
            "date_heure": (timezone.now() + timedelta(days=1)).isoformat(),
            "duree": 30,
            "statut": "prévu"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class NotificationViewTests(AuthenticatedTestCase):
    def setUp(self):
        self.authenticate(role="client")  # L'utilisateur client va lire ses notifications
        self.url = reverse('notification-list')
        Notification.objects.create(destinataire=self.user, message="Test")

    def test_notification_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


 # Désactivé temporairement : la logique métier n'existe pas encore

"""class IntegrationViewTests(AuthenticatedTestCase):
    def setUp(self):
        self.specialiste = CustomUser.objects.create_user(username="spec", password="pass", role="specialiste")
        self.client_user = CustomUser.objects.create_user(username="client", password="pass", role="client")
        self.authenticate(role="specialiste")
        self.url = reverse('rendezvous-list')

    def test_rendezvous_triggers_notification(self):
        data = {
            "client": self.client_user.id,
            "specialiste": self.specialiste.id,
            "date_heure": (timezone.now() + timedelta(hours=1)).isoformat(),
            "duree": 30,
            "statut": "prévu"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Notification.objects.filter(destinataire=self.client_user).exists())#
"""

