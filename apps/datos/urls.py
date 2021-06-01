from django.urls import path
from . import views

app_name = 'datos_app'

urlpatterns = [
    path('datos', views.datos.as_view(), name='datos'),
    path('datos/ejemplo-1', views.ejemplo1.as_view(), name='ejemplo1'),
    path('datos/ejemplo-2', views.ejemplo2.as_view(), name='ejemplo2'),
    path('datos/ejemplo-3', views.ejemplo3.as_view(), name='ejemplo3'),
    path('datos/ejemplo-4', views.ejemplo4.as_view(), name='ejemplo4'),
    path('datos/ejemplo-5', views.ejemplo5.as_view(), name='ejemplo5'),
    path('datos/ejemplo-6', views.ejemplo6.as_view(), name='ejemplo6'),
]