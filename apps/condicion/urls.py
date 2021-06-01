from django.urls import path
from . import views

app_name = 'condicion_app'

urlpatterns = [
    path('condicion', views.condicion.as_view(), name='condicion'),
    path('condicion/ejemplo-1', views.ejemplo1.as_view(), name='ejemplo1'),
    path('condicion/ejemplo-2', views.ejemplo2.as_view(), name='ejemplo2'),
    path('condicion/ejemplo-3', views.ejemplo3.as_view(), name='ejemplo3'),
    path('condicion/ejemplo-4', views.ejemplo4.as_view(), name='ejemplo4'),
    path('condicion/ejemplo-5', views.ejemplo5.as_view(), name='ejemplo5'),
    path('condicion/ejemplo-6', views.ejemplo6.as_view(), name='ejemplo6'),
]