from datetime import datetime
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template

def hola(request):
    return HttpResponse('<h1>Hola mundo</h1>')
def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'<h2>La fecha y hora actual es {fecha_actual}</h2>')
def calcular_fecha_nacimiento(request, edad):
    fecha=  datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento para tus {edad} a;os seria {fecha}')
def mi_template(request):

    cargar_archivo = open(r'C:\Users\Julian\Desktop\coder\mvc-entrega\templates\templated.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close
    contexto =  Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)