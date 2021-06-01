from django.urls import path
from . import views

app_name = 'repetitivas_app'

urlpatterns = [
    path('repetitivas', views.repetitivas.as_view(), name='repetitivas'),
    path('repetitivas/ejemplo-1', views.ejemplo1.as_view(), name='ejemplo1'),
    path('repetitivas/ejemplo-2', views.ejemplo2.as_view(), name='ejemplo2'),
    path('repetitivas/ejemplo-3', views.ejemplo3.as_view(), name='ejemplo3'),
    path('repetitivas/ejemplo-4', views.ejemplo4.as_view(), name='ejemplo4'),
    path('repetitivas/ejemplo-5', views.ejemplo5.as_view(), name='ejemplo5'),
    path('repetitivas/ejemplo-6', views.ejemplo6.as_view(), name='ejemplo6'),
]