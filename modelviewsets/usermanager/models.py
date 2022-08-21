from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Importation de notre manager utilisateur customiser 
from .managers import CustomUserManager
# Déclaration de nos modeles avec lesquels les données seront capturées

# on utilise ici AbstractBaseUser pour pouvoir faire un model utilisateur personnalisé
class Utilisateur(AbstractBaseUser,PermissionsMixin):
    
    email = models.EmailField(unique=True, error_messages={'unique':("L'email existe déjà!")})
    username = None # suppression du champ username car nous n'en avons pas besoin
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = "email" # on specifie ici que notre champ username est notre email
    REQUIRED_FIELDS =  []
    
    objects = CustomUserManager() # Specification que tous les objets de la clasee proviennent du CustomUserManager
    
    # La classe ci-dessous permet de mapper le model vers un schema postgresql predefinit
    class Meta:
        managed = True
        db_table = 'utilisateurs\".\"users'

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True