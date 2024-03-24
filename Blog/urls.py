from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', InicioSesion, name='login'),
    path('registro/', Registro, name='registro'),
    path("logout/", logout, name="logout"),
    path('',Inicio ,name="inicio" ),


    #####CRUD --- CREATE
    path("new_manga/", Subir_Manga, name="nuevoM"),
    path("new_anime/", Subir_Anime, name="nuevoA"),
    path("new_video/", Subir_VideoJuego, name="nuevoV"),



    #####CRUD --- READ
    path("view_mangas/", VerMangas, name="verM"),
    path("view_animes/", VerAnimes, name="verA"),
    path("view_videojuegos/", VerMangas, name="verV"),


    #####CRUD --- UPDATE
    path("up_manga/<tituloManga>/", editarManga, name="editarM"),
    path("up_anime/<tituloAnime>/", editarAnime, name="editarA"),
    path("up_manga/<tituloManga>/", editarVideo, name="editarV"),


    #####CRUD --- DELETE
    path("del_manga/<tituloManga>/", borrarM, name="borrarM"),
    path("del_anime/<tituloAnime>/", borrarA, name="borrarA"),
    path("del_videojuego/<tituloVideojuego>/", borrarV, name="borrarV"),
]