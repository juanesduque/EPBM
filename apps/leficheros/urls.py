from django.urls import path
from . import views

app_name = 'leficheros_app'

urlpatterns = [
    path('leficheros', views.leficheros.as_view(), name='leficheros'),
    path('leficheros/ejemplo-1', views.ejemplo1.as_view(), name='ejemplo1'),
    path('leficheros/ejemplo-2', views.ejemplo2.as_view(), name='ejemplo2'),
    path('leficheros/ejemplo-3', views.ejemplo3.as_view(), name='ejemplo3'),
    path('leficheros/ejemplo-4', views.ejemplo4.as_view(), name='ejemplo4'),
    path('leficheros/ejemplo-5', views.ejemplo5.as_view(), name='ejemplo5'),
    path('leficheros/ejemplo-6', views.ejemplo6.as_view(), name='ejemplo6'),
]