from .models import Utilisateur
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from usermanager import serializers,models
from .serializers import SignupSerializer,UtilisateurSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer
from rest_framework.viewsets import ModelViewSet

"""classe serializer multiple"""
class MultipleSerializerMixin:
    detail_serializer_class = None
    def get_serializer_class(self):
        if self.action == "retrive" and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

"""Vue Utilisateur"""
class UtilisateurViewSet(MultipleSerializerMixin, ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UtilisateurSerializer
    def get_queryset(self):
        return models.Utilisateur.objects.all()

"""Vue d'inscription de l'utilisateur"""
class SignupAPIView(APIView):
      
    permission_classes = []    
    
    def post(self, request):
        password = request.POST.get('password', None)
        confirm_password = request.POST.get('confirm_password', None)
        if password == confirm_password: 
            serializer = SignupSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = serializer.data
            response = status.HTTP_201_CREATED
        else:
            data = ''
            raise ValidationError({'password_mismatch': 'Les champs de mot de passe de concordent pas!'})    
        return Response(data, status=response)

"""Vue de login autrement dit c'est la vue qui va nous permettre 
de nous authentifier et obtenir les token access et refresh"""    
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer    