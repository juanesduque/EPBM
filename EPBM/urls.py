from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.clases.urls')),
    path('', include('apps.command_window.urls')),
    path('', include('apps.condicion.urls')),
    path('', include('apps.datos.urls')),
    path('', include('apps.esdatos.urls')),
    path('', include('apps.funciones.urls')),
    path('', include('apps.ledatos.urls')),
    path('', include('apps.leficheros.urls')),
    path('', include('apps.main.urls')),
    path('', include('apps.matrices.urls')),
    path('', include('apps.operadores.urls')),
    path('', include('apps.repetitivas.urls')),
    path('', include('apps.workspace.urls')),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)