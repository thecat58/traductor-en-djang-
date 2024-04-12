from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from .serializer import CustomTokenResponseSerializer, palabraSerializer
from rest_framework.response import Response

from .forms import SignUpForm
from .models import TraduccionPalabra
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView



def traductor(request):
    
    return render (request, "traductor/login.html")

def cerrar_sesion(request):
    logout(request)
    # Redirige a una página de inicio o a donde desees después del cierre de sesión
    return redirect('/traductor/')


def traducir_palabra(request):
    traduccion = None
    if request.method == 'POST':
        palabra_usuario = request.POST.get('palabra', None)
        if palabra_usuario:
            # Buscar la traducción en la base de datos
            resultado = TraduccionPalabra.objects.filter(palabra=palabra_usuario).first()
            if resultado:
                traduccion = resultado.traduccion
    return render(request, 'traductor/traductor.html', {'traduccion': traduccion})


def traducir_palabra2(request):
    palabra = None
    if request.method == 'POST':
        traduccion_usuario = request.POST.get('traduccion', None)
        if traduccion_usuario:
            # Buscar la palabra correspondiente en la base de datos
            resultado = TraduccionPalabra.objects.filter(traduccion=traduccion_usuario).first()
            if resultado:
                palabra = resultado.palabra
    return render(request, 'traductor/traductor2.html', {'palabra': palabra})


class TraduccionPalabraListView(ListView):
    model = TraduccionPalabra
    template_name = 'traductor/palabra_crud.html'  # Ruta al archivo HTML donde se mostrará la lista de traducciones

class TraduccionPalabraDetailView(DetailView):
    model = TraduccionPalabra
    template_name = 'traductor/palabra_crud.html'  # Ruta al archivo HTML donde se mostrará el detalle de una traducción

class TraduccionPalabraCreateView(CreateView):
    model = TraduccionPalabra
    fields = ['palabra', 'traduccion']
    template_name = 'traductor/palabra_crud.html'
    success_url = reverse_lazy('palabra-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class TraduccionPalabraUpdateView(UpdateView):
    model = TraduccionPalabra
    fields = ['palabra', 'traduccion']
    template_name = 'traductor/palabra_crud.html'  # Esta es la misma plantilla que usas para crear una nueva palabra
    success_url = reverse_lazy('palabra-list')  # Redirige a la lista de palabras después de actualizar una palabra

class TraduccionPalabraDeleteView(DeleteView):
    model = TraduccionPalabra
    success_url = reverse_lazy('palabra-list') 

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/login/')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Cambia 'home' por el nombre de la URL a la que quieres redirigir al usuario después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Cambia 'home' por el nombre de la URL a la que quieres redirigir al usuario después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Cambia 'login' por el nombre de la URL de tu página de inicio de sesión


# apis
class palabraViewSet(viewsets.ModelViewSet):
    queryset = TraduccionPalabra.objects.all() 
    serializer_class = palabraSerializer
   

