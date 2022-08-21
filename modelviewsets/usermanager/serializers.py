from rest_framework import serializers,fields
from.models import Utilisateur
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

""" serializer de l'utilisateur qui va nous permettre d'afficher la liste des
utilisateurs"""
class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Utilisateur
        fields = ['id', 'email', 'is_active','is_staff']
        
class SignupSerializer(serializers.ModelSerializer):
    """
        Serializer pour créer un nouvel utilisateur d'inscription   
    """
    class Meta:
          model = Utilisateur
          fields = ['id', 'email', 'password']
          extra_kwargs = {'password': {'write_only': True}} 
    
    def create(self, validated_data): 
    
        if validate_password(validated_data['password']) == None:
               password = make_password(validated_data['password'])                                         
               user = Utilisateur.objects.create(
                      email=validated_data['email'],
                      password=password
        )
        
        return user

"""serializer de creation de token"""

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        return token