from rest_framework import serializers
from django.contrib.auth.models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import TraduccionPalabra

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        # Serializar el usuario para incluir todos los detalles en la respuesta
        user_serializer = UserSerializer(user)
        
        return Response({'token': token.key, 'user': user_serializer.data})

# Serializador de Departamento


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

 
class CustomTokenResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class palabraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraduccionPalabra
        fields = '__all__'


