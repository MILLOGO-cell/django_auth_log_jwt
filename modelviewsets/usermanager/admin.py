from django.contrib.auth import get_user_model 
from django.contrib import admin

Utilisateur = get_user_model()
admin.site.register(Utilisateur) 
