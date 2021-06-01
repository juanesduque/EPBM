from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class condicion(TemplateView):
    template_name = 'teoria/condicion/condicion.html'

class ejemplo1(TemplateView):
    template_name = 'teoria/condicion/ejemplos/ejemplo1.html'

class ejemplo2(TemplateView):
    template_name = 'teoria/condicion/ejemplos/ejemplo2.html'

class ejemplo3(TemplateView):
    template_name = 'teoria/condicion/ejemplos/ejemplo3.html'

class ejemplo4(TemplateView):
    template_name = 'teoria/condicion/ejemplos/ejemplo4.html'

class ejemplo5(TemplateView):
    template_name = 'teoria/condicion/ejemplos/ejemplo5.html'

class ejemplo6(TemplateView):
    template_name = 'teoria/condicion/ejemplos/ejemplo6.html'