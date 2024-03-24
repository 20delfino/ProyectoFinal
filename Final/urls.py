from django.contrib import admin
from django.urls import path, include
from Blog.views import *
from django.conf import settings
from django.conf.urls.static import static  # Importa static desde django.conf.urls.static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio, name="inicio"),
    path('', include('Blog.urls')),
]

# Agrega las URL de archivos estáticos solo en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
