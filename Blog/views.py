from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from Blog.models import *
from django.urls import reverse
from django.contrib.auth import logout as django_logout
from Blog.forms import *
from django.db.models import OneToOneField
from django.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
def InicioSesion(request):
    form = AuthenticationForm()
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario= form.cleaned_data["username"]
            contra= form.cleaned_data["password"]
            user= authenticate(username=usuario, password=contra)
            if user:
                login(request, user)
                return render(request,"Blog/Baseinicio.html", {"titulo": f"Bienvenido{user}"})
        else:
               return render(request,"Blog/login.html", {"titulo": "Datos no validos", "subtitulo": "Ingrese nuevamente", "formulario":form})
    else:
        return render(request,"Blog/login.html", {"titulo":"Inicio de sesion", "subtitulo": "Ingrese sus datos","formulario":form})

def Registro(request):
    form = usuarioRegistro()
    if request.method=="POST":
        form = usuarioRegistro(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request,"Blog/Baseinicio.html", {"titulo": "Usuario creado correctamente"})
    return render(request,"Blog/registro.html", {"titulo":"Registro de nuevos usuarios", "subtitulo": "Ingrese sus datos","formulario":form})

def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse('inicio'))

def Inicio(request):
     return render(request, 'Blog/Baseinicio.html')

def Subir_Manga(request):
    form = Manga_Form()
    if  request.POST:
        form= Manga_Form(request.POST, request.FILES)
        if form.is_valid():
            info_dict= form.cleaned_data
            nuevo_manga= Manga(titulo=info_dict["titulo"],
                               fecha_pub=info_dict["fecha_pub"], 
                               genero=info_dict["genero"],
                               img=info_dict["img"])
            nuevo_manga.save()
            return render(request, 'Blog/Baseinicio.html', {"titulo":"Tu manga se ha subido correctamente", "subtitulo": "Continua explorando la pagina"})
        else:
            form = Manga_Form()
    return render(request, 'Blog/new_manga.html', {"titulo":"Subir Nuevo Manga", "subtitulo": "Llena todos los campos","formulario":form})

def Subir_Anime(request):
    form = Anime_Form()
    if  request.POST:
        form= Anime_Form(request.POST, request.FILES)
        if form.is_valid():
            info_dict= form.cleaned_data
            nuevo_anime= Anime(titulo=info_dict["titulo"],
                               fecha_emi=info_dict["fecha_emi"], 
                               genero=info_dict["genero"],
                               img=info_dict["img"])
            nuevo_anime.save()
            return render(request, 'Blog/Baseinicio.html', {"titulo":"Tu Anime se ha subido correctamente", "subtitulo": "Continua explorando la pagina"})
        else:
            form = Anime_Form()
    return render(request, 'Blog/new_anime.html', {"titulo":"Subir Nuevo Anime", "subtitulo": "Llena todos los campos","formulario":form})

def Subir_VideoJuego(request):
    form = Videojuego_Form()
    if  request.POST:
        form= Videojuego_Form(request.POST, request.FILES)
        if form.is_valid():
            info_dict= form.cleaned_data
            nuevo_video= Videojuego(titulo=info_dict["titulo"],
                               fecha_pub=info_dict["fecha_pub"], 
                               genero=info_dict["genero"],
                               consola=info_dict["consola"],
                               img=info_dict["img"])
            nuevo_video.save()
            return render(request, 'Blog/Baseinicio.html', {"titulo":"Tu videojuego se ha subido correctamente", "subtitulo": "Continua explorando la pagina"})
        else:
            form = Manga_Form()
    return render(request, 'Blog/new_video.html', {"titulo":"Subir Nuevo Videojuego", "subtitulo": "Llena todos los campos","formulario":form})


def VerMangas(request):
    mangas=Manga.objects.all()
    return render(request, 'Blog/view_mangas.html', {"titulo":"Aqui puedes ver los mangas que han subido", "subtitulo": "Echale un ojo","biblioteca":mangas})

def VerAnimes(request):
    animes=Anime.objects.all()
    return render(request, 'Blog/view_animes.html', {"titulo":"Aqui puedes ver los animes que han subido", "subtitulo": "Echale un ojo","biblioteca":animes})

def VerVideo(request):
    videojuegos=Videojuego.objects.all()
    return render(request, 'Blog/view_videojuegos.html', {"titulo":"Aqui puedes ver los videojuegos que han subido", "subtitulo": "Echale un ojo","biblioteca":videojuegos})

def borrarM(request,tituloManga):
    manga= Manga.objects.get(titulo=tituloManga)
    manga.delete()
    mangas= Manga.objects.all()
    return render(request, 'Blog/view_mangas.html', {"titulo":"Aqui puedes ver los mangas que han subido", "subtitulo": "Echale un ojo","biblioteca":mangas})

def borrarA(request,tituloAnime):
    animes= Anime.objects.get(titulo=tituloAnime)
    animes.delete()
    mangas= Anime.objects.all()
    return render(request, 'Blog/view_animes.html', {"titulo":"Aqui puedes ver los mangas que han subido", "subtitulo": "Echale un ojo","biblioteca":animes})


def borrarV(request,tituloVideojuego):
    videojuegos= Videojuego.objects.get(titulo=tituloVideojuego)
    videojuegos.delete()
    mangas= Videojuego.objects.all()
    return render(request, 'Blog/view_videos.html', {"titulo":"Aqui puedes ver los mangas que han subido", "subtitulo": "Echale un ojo","biblioteca":videojuegos})

def editarManga(request, tituloManga):
    manga= Manga.objects.get(titulo=tituloManga)
    form = Manga_Form()
    if  request.method=="POST":
        form= Manga_Form(request.POST, request.FILES)
        if form.is_valid():
            info_dict= form.cleaned_data
            manga.titulo=info_dict["titulo"]
            manga.fecha_pub=info_dict["fecha_pub"]
            manga.genero=info_dict["genero"]
            manga.img=info_dict["img"]
            manga.save()
            return render(request, 'Blog/Baseinicio.html', {"titulo":"Los datos del manga han sido actualizados", "subtitulo": "Continua explorando la pagina"})
        else:
            form = Manga_Form(initial={"titulo":manga.titulo,"fecha de publicacion":manga.fecha_pub,"genero":manga.genero,"imagen":manga.img})
    return render(request, 'Blog/up_manga.html', {"titulo":"Editar Manga", "subtitulo": "Para editar el titulo, llena todos los campos","formulario":form, "titulo":tituloManga})


def editarAnime(request, tituloAnime):
    anime= Anime.objects.get(titulo=tituloAnime)
    form = Anime_Form()
    if  request.method=="POST":
        form= Anime_Form(request.POST, request.FILES)
        if form.is_valid():
            info_dict= form.cleaned_data
            anime.titulo=info_dict["titulo"]
            anime.fecha_emi=info_dict["fecha_emi"]
            anime.genero=info_dict["genero"]
            anime.img=info_dict["img"]
            anime.save()
            return render(request, 'Blog/Baseinicio.html', {"titulo":"Los datos del anime han sido actualizados", "subtitulo": "Continua explorando la pagina"})
        else:
            form = Anime_Form(initial={"titulo":anime.titulo,"fecha de emision":anime.fecha_emi,"genero":anime.genero,"imagen":anime.img})
    return render(request, 'Blog/up_anime.html', {"titulo":"Editar Anime", "subtitulo": "Para editar el titulo, llena todos los campos","formulario":form, "titulo":tituloAnime})


def editarVideo(request, tituloVideojuego):
    videojuegos= Videojuego.objects.get(titulo=tituloVideojuego)
    form = Videojuego_Form()
    if  request.method=="POST":
        form= Videojuego_Form(request.POST, request.FILES)
        if form.is_valid():
            info_dict= form.cleaned_data
            videojuegos.titulo=info_dict["titulo"]
            videojuegos.fecha_pub=info_dict["fecha_pub"]
            videojuegos.genero=info_dict["genero"]
            videojuegos.img=info_dict["img"]
            videojuegos.save()
            return render(request, 'Blog/Baseinicio.html', {"titulo":"Los datos del videojuego han sido actualizados", "subtitulo": "Continua explorando la pagina"})
        else:
            form = Videojuego_Form(initial={"titulo":videojuegos.titulo,"fecha de publicacion":videojuegos.fecha_pub,"genero":videojuegos.genero,"imagen":videojuegos.img})
    return render(request, 'Blog/up_video.html', {"titulo":"Editar Manga", "subtitulo": "Llena todos los campos para editar el titulo","formulario":form, "titulo":tituloVideojuego})


