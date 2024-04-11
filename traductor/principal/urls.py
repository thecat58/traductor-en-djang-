from django.urls import path


from .views import TraduccionPalabraCreateView, TraduccionPalabraDeleteView, TraduccionPalabraDetailView, TraduccionPalabraListView, TraduccionPalabraUpdateView, traductor
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('', TraduccionPalabraListView.as_view(), name='palabra-detail'),
    path('palabra/<int:pk>/', TraduccionPalabraDetailView.as_view(),
         name='palabra_crut'),
    path('palabra-create/', TraduccionPalabraCreateView.as_view(),
         name='palabra-create'),
    path('palabra/<int:pk>/update/',
         TraduccionPalabraUpdateView.as_view(), name='palabra-update'),
    path('palabra/<int:pk>/delete/',
         TraduccionPalabraDeleteView.as_view(), name='palabra-delete'),
     path('traductor/',
         traductor, name='traductor'),

    # URL para la vista de registro (register)


]
