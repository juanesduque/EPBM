from django.urls import path
from . import views

app_name = 'esdatos_app'

urlpatterns = [
    path('esdatos', views.esdatos.as_view(), name='esdatos'),
    path('esdatos/ejemplo-1', views.ejemplo1.as_view(), name='ejemplo1'),
    path('esdatos/ejemplo-2', views.ejemplo2.as_view(), name='ejemplo2'),
    path('esdatos/ejemplo-3', views.ejemplo3.as_view(), name='ejemplo3'),
    path('esdatos/ejemplo-4', views.ejemplo4.as_view(), name='ejemplo4'),
    path('esdatos/ejemplo-5', views.ejemplo5.as_view(), name='ejemplo5'),
    path('esdatos/ejemplo-6', views.ejemplo6.as_view(), name='ejemplo6'),
]