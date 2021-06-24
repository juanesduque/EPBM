from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class proyecto2(TemplateView):
    template_name = 'proyectos/proyecto2/proyecto2.html'