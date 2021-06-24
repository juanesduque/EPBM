from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class proyecto1(TemplateView):
    template_name = 'proyectos/proyecto1/proyecto1.html'