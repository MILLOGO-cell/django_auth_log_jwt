from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _ 

class CustomUserManager(BaseUserManager):
    """
    Modele utilisateur customiser, l'email est l'unique identifiant pour l'authentification
    au lieu de username
    """
    def create_user(self, email, password, **extra_fields):
        """
        créer et sauvegarder un utilisateur en donnant l'email et le password
        """
        if not email:
            raise ValueError(_("L'email doit être saisi!"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
        
    def create_superuser(self, email, password, **extra_fields):
        """Créer et sauvegarder un super utilisateur en donnant l'email et le 
        password"""
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Le super utilisateur doit avoir is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Le super utilisateur doit avoir is_superuser=True'))
        return self.create_user(email, password, **extra_fields)