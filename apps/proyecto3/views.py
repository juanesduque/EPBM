from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class proyecto3(TemplateView):
    template_name = 'proyectos/proyecto3/proyecto3.html'