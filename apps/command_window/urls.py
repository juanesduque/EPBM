from django.urls import path
from . import views

app_name = 'command_window_app'

urlpatterns = [
    path('command_window', views.command_window.as_view(), name='command_window'),
    path('command_window/ejemplo-1', views.ejemplo1.as_view(), name='ejemplo1'),
    path('command_window/ejemplo-2', views.ejemplo2.as_view(), name='ejemplo2'),
    path('command_window/ejemplo-3', views.ejemplo3.as_view(), name='ejemplo3'),
    path('command_window/ejemplo-4', views.ejemplo4.as_view(), name='ejemplo4'),
    path('command_window/ejemplo-5', views.ejemplo5.as_view(), name='ejemplo5'),
    path('command_window/ejemplo-6', views.ejemplo6.as_view(), name='ejemplo6'),
]