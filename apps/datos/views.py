from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class datos(TemplateView):
    template_name = 'teoria/datos/datos.html'

class ejemplo1(TemplateView):
    template_name = 'teoria/datos/ejemplos/ejemplo1.html'

class ejemplo2(TemplateView):
    template_name = 'teoria/datos/ejemplos/ejemplo2.html'

class ejemplo3(TemplateView):
    template_name = 'teoria/datos/ejemplos/ejemplo3.html'

class ejemplo4(TemplateView):
    template_name = 'teoria/datos/ejemplos/ejemplo4.html'

class ejemplo5(TemplateView):
    template_name = 'teoria/datos/ejemplos/ejemplo5.html'

class ejemplo6(TemplateView):
    template_name = 'teoria/datos/ejemplos/ejemplo6.html'