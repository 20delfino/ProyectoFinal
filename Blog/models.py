from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/avatars/', null=True,blank=True)

    def __str__(self):
        return self.user

class Manga(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_pub= models.DateField()
    genero=models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/manga_images/', null=True,blank=True)

    def __str__(self):
        return self.titulo


class Anime(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_emi= models.DateField()
    genero=models.CharField(max_length=100)
    img = models.ImageField(upload_to='manga_images/', null=True,blank=True)

    def __str__(self):
        return self.titulo

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_pub= models.DateField()
    genero=models.CharField(max_length=100)
    consola= models.CharField(max_length=100)
    img = models.ImageField(upload_to='manga_images/', null=True,blank=True)
    def __str__(self):
        return self.titulo
