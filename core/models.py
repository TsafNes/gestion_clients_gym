from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('gestionnaire', 'Gestionnaire'),
        ('specialiste', 'Spécialiste'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class Abonnement(models.Model):
    type = models.CharField(max_length=45)
    duree = models.IntegerField()
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"{self.type} ({self.date_debut} → {self.date_fin})"


class Gestionnaire(models.Model):
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    identifiant = models.CharField(max_length=45, unique=True)
    mot_de_passe = models.CharField(max_length=128)  # hashé de préférence

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Client(models.Model):
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    telephone = models.CharField(max_length=45)
    courriel = models.CharField(max_length=45)
    nb_heures_restantes = models.IntegerField()
    abonnement = models.ForeignKey(Abonnement, on_delete=models.SET_NULL, null=True)
    gestionnaire = models.ForeignKey(Gestionnaire, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Specialiste(models.Model):
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    telephone = models.CharField(max_length=45)
    identifiant = models.CharField(max_length=45, unique=True)
    mot_de_passe = models.CharField(max_length=128)  # hashé de préférence
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    abonnement = models.ForeignKey(Abonnement, on_delete=models.SET_NULL, null=True)
    gestionnaire = models.ForeignKey(Gestionnaire, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class RendezVous(models.Model):
    STATUT_CHOICES = [
        ('prévu', 'Prévu'),
        ('annulé', 'Annulé'),
        ('terminé', 'Terminé'),
    ]

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='rendezvous_client',
        on_delete=models.CASCADE
    )
    specialiste = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='rendezvous_specialiste',
        on_delete=models.CASCADE
    )
    date_heure = models.DateTimeField()
    duree = models.IntegerField(help_text="Durée en minutes")
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='prévu')

    def clean(self):
        conflits = RendezVous.objects.filter(
            specialiste=self.specialiste,
            date_heure__lt=self.date_heure + timezone.timedelta(minutes=self.duree),
            date_heure__gt=self.date_heure - timezone.timedelta(minutes=self.duree)
        ).exclude(pk=self.pk)

        if conflits.exists():
            raise ValidationError("Conflit : le spécialiste a déjà un rendez-vous à ce moment.")


class Notification(models.Model):
    destinataire = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification pour {self.destinataire.username} : {self.message[:20]}"
