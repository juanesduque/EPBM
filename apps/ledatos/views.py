from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ledatos(TemplateView):
    template_name = 'teoria/ledatos/ledatos.html'

class ejemplo1(TemplateView):
    template_name = 'teoria/ledatos/ejemplos/ejemplo1.html'

class ejemplo2(TemplateView):
    template_name = 'teoria/ledatos/ejemplos/ejemplo2.html'

class ejemplo3(TemplateView):
    template_name = 'teoria/ledatos/ejemplos/ejemplo3.html'

class ejemplo4(TemplateView):
    template_name = 'teoria/ledatos/ejemplos/ejemplo4.html'

class ejemplo5(TemplateView):
    template_name = 'teoria/ledatos/ejemplos/ejemplo5.html'

class ejemplo6(TemplateView):
    template_name = 'teoria/ledatos/ejemplos/ejemplo6.html'