from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class proyecto4(TemplateView):
    template_name = 'proyectos/proyecto4/proyecto4.html'