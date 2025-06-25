from django.test import TestCase
from core.models import Abonnement, Client, Gestionnaire, RendezVous, Notification, CustomUser
from datetime import date, datetime, timedelta
from django.utils import timezone

class AbonnementModelTest(TestCase):
    def test_str_representation(self):
        abonnement = Abonnement.objects.create(
            type="Mensuel",
            duree=30,
            date_debut=date.today(),
            date_fin=date.today() + timedelta(days=30)
        )
        self.assertIn("Mensuel", str(abonnement))

class ClientModelTest(TestCase):
    def setUp(self):
        self.abonnement = Abonnement.objects.create(
            type="Test",
            duree=15,
            date_debut=date.today(),
            date_fin=date.today() + timedelta(days=15)
        )
        self.gestionnaire = Gestionnaire.objects.create(
            nom="Doe",
            prenom="John",
            identifiant="gestionnaire1",
            mot_de_passe="test"
        )

    def test_str_representation(self):
        client = Client.objects.create(
            nom="Test",
            prenom="Client",
            telephone="123456",
            courriel="client@example.com",
            nb_heures_restantes=10,
            abonnement=self.abonnement,
            gestionnaire=self.gestionnaire
        )
        self.assertEqual(str(client), "Client Test")

class RendezVousModelTest(TestCase):
    def setUp(self):
        self.client = CustomUser.objects.create_user(username="client1", password="pass", role="client")
        self.specialiste = CustomUser.objects.create_user(username="spec1", password="pass", role="specialiste")

    def test_no_conflit(self):
        rv = RendezVous.objects.create(
            client=self.client,
            specialiste=self.specialiste,
            date_heure=timezone.now() + timedelta(hours=1),
            duree=30,
            statut='prévu'
        )
        self.assertEqual(rv.statut, 'prévu')

class NotificationModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="notified", password="pass", role="client")

    def test_notification_str(self):
        notif = Notification.objects.create(
            destinataire=self.user,
            message="Test message"
        )
        self.assertIn("Notification pour", str(notif))

class CustomUserModelTest(TestCase):
    def test_create_custom_user(self):
        user = CustomUser.objects.create_user(username="testuser", password="pass123", role="gestionnaire")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.role, "gestionnaire")
        self.assertTrue(user.check_password("pass123"))
