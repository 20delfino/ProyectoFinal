from django.forms import *
from .models import *  # Asegúrate de importar el modelo correspondiente
from django.db.models import OneToOneField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Create your models here.
class usuarioRegistro(UserCreationForm):
    email=forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2"]



class Perfil_Form(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['user','avatar']  # Puedes especificar los campos que quieres incluir en el formulario



class Manga_Form(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['titulo', 'fecha_pub', 'genero', 'img']


class Anime_Form(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['titulo', 'fecha_emi', 'genero', 'img']

class Videojuego_Form(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['titulo', 'fecha_pub', 'genero', 'consola', 'img']