from rest_framework import viewsets, permissions
from rest_framework.exceptions import NotAuthenticated
from .models import Client, Gestionnaire, Specialiste, Abonnement, RendezVous, Notification
from .serializers import (
    ClientSerializer, GestionnaireSerializer, SpecialisteSerializer,
    AbonnementSerializer, RendezVousSerializer, NotificationSerializer
)
from .permissions import IsClient, IsGestionnaire, IsSpecialiste


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, IsGestionnaire]  # 🔒 Seuls les gestionnaires accèdent aux clients


class GestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Gestionnaire.objects.all()
    serializer_class = GestionnaireSerializer
    permission_classes = [permissions.IsAuthenticated, IsGestionnaire]  # 🔒 Accès réservé aux gestionnaires


class SpecialisteViewSet(viewsets.ModelViewSet):
    queryset = Specialiste.objects.all()
    serializer_class = SpecialisteSerializer
    permission_classes = [permissions.IsAuthenticated, IsGestionnaire]  # 🔒 Accès réservé aux gestionnaires


class AbonnementViewSet(viewsets.ModelViewSet):
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer
    permission_classes = [permissions.IsAuthenticated, IsGestionnaire]  # 🔒 Gestion des abonnements par les gestionnaires


class RendezVousViewSet(viewsets.ModelViewSet):
    queryset = RendezVous.objects.all()
    serializer_class = RendezVousSerializer
    permission_classes = [permissions.IsAuthenticated]  # 🔒 Tous les rôles peuvent voir leurs rendez-vous
    # Tu peux filtrer selon le rôle ici si tu veux


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated, IsClient]  # 🔒 Seuls les clients consultent leurs notifications

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            raise NotAuthenticated("Vous devez être connecté pour accéder à vos notifications.")
        return Notification.objects.filter(destinataire=user).order_by('-date')
