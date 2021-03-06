from django.urls import path
from . import views

app_name = 'clases_app'

urlpatterns = [
    path('clases', views.clases.as_view(), name='clases'),
    path('clases/ejemplo-1', views.ejemplo1.as_view(), name='ejemplo1'),
    path('clases/ejemplo-2', views.ejemplo2.as_view(), name='ejemplo2'),
    path('clases/ejemplo-3', views.ejemplo3.as_view(), name='ejemplo3'),
    path('clases/ejemplo-4', views.ejemplo4.as_view(), name='ejemplo4'),
    path('clases/ejemplo-5', views.ejemplo5.as_view(), name='ejemplo5'),
    path('clases/ejemplo-6', views.ejemplo6.as_view(), name='ejemplo6'),
]