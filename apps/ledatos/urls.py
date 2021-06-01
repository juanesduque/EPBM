from django.urls import path
from . import views

app_name = 'ledatos_app'

urlpatterns = [
    path('ledatos', views.ledatos.as_view(), name='ledatos'),
    path('ledatos/ejemplo-1', views.ejemplo1.as_view(), name='ejemplo1'),
    path('ledatos/ejemplo-2', views.ejemplo2.as_view(), name='ejemplo2'),
    path('ledatos/ejemplo-3', views.ejemplo3.as_view(), name='ejemplo3'),
    path('ledatos/ejemplo-4', views.ejemplo4.as_view(), name='ejemplo4'),
    path('ledatos/ejemplo-5', views.ejemplo5.as_view(), name='ejemplo5'),
    path('ledatos/ejemplo-6', views.ejemplo6.as_view(), name='ejemplo6'),
]