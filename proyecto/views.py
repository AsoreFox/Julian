from curses.ascii import HT
from datetime import datetime
from email.policy import HTTP
from re import template
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
import random
from home.models import Persona

def hola(request):
    return HttpResponse('<h1>Hola mundo</h1>')

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'<h2>La fecha y hora actual es {fecha_actual}</h2>')
    
def calcular_fecha_nacimiento(request, edad):
    fecha=  datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento para tus {edad} a;os seria {fecha}')

def mi_template(request,):
    template = loader.get_template('mi_template.html')
    template_renderizado = template.render()
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):
    template = loader.get_template('tu_template.html')
    template_renderizado = template.render({'persona': nombre})
    return HttpResponse(template_renderizado)

def prueba_template(request):
    mi_contexto = {
        'rango': list(range(1,11)),
        'valor_aleatorio' : random.randrange(1,11)
        }
    template =  loader.get_template('prueba_template.html')
    template_renderizado = template.render (mi_contexto)

    return HttpResponse(template_renderizado)

def crear_personas(request, nombre, apellido):

    personas = Persona(nombre = nombre, apellido = apellido, edad = random.randrange(1,99),  nacimiento = datetime.now())
    personas.save()
    template = loader.get_template('crear_personas.html')
    template_renderizado = template.render({'personas': personas})

    return HttpResponse(template_renderizado)

def ver_personas(request):
    personas = Persona.objects.all()
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas': personas})

    return HttpResponse(template_renderizado)
