from django.urls import path
from . import views

app_name = 'workspace_app'

urlpatterns = [
    path('workspace', views.workspace.as_view(), name='workspace'),
    path('workspace/ejemplo-1', views.ejemplo1.as_view(), name='ejemplo1'),
    path('workspace/ejemplo-2', views.ejemplo2.as_view(), name='ejemplo2'),
    path('workspace/ejemplo-3', views.ejemplo3.as_view(), name='ejemplo3'),
    path('workspace/ejemplo-4', views.ejemplo4.as_view(), name='ejemplo4'),
    path('workspace/ejemplo-5', views.ejemplo5.as_view(), name='ejemplo5'),
    path('workspace/ejemplo-6', views.ejemplo6.as_view(), name='ejemplo6'),
]