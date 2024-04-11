from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static

from principal.views import *
from .serializer import CustomAuthToken


router = routers.DefaultRouter()

router.register(r'palabras', palabraViewSet, basename='TraduccionPalabra')








# Define las rutas
urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomAuthToken.as_view()),
]