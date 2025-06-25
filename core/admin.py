from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser, Abonnement, Gestionnaire,
    Client, Specialiste, RendezVous, Notification
)

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Abonnement)
admin.site.register(Gestionnaire)
admin.site.register(Client)
admin.site.register(Specialiste)
admin.site.register(RendezVous)
admin.site.register(Notification)
