from rest_framework import serializers
from .models import Client, Gestionnaire, Specialiste, Abonnement, RendezVous, Notification

class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonnement
        fields = '__all__'

class GestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestionnaire
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class SpecialisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialiste
        fields = '__all__'

class RendezVousSerializer(serializers.ModelSerializer):
    class Meta:
        model = RendezVous
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'