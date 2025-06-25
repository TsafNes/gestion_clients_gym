from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, GestionnaireViewSet, SpecialisteViewSet, AbonnementViewSet, RendezVousViewSet
from .views import NotificationViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'gestionnaires', GestionnaireViewSet)
router.register(r'specialistes', SpecialisteViewSet)
router.register(r'abonnements', AbonnementViewSet)
router.register(r'rendezvous', RendezVousViewSet)
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]
