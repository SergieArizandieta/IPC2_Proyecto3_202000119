from django.http import HttpRequest
from django.http.response import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido= apellido

def saludo(request):

    return HttpResponse("""
    <html>
    <body>
    <h1> Hola alumnos esta es nuestra primera pagina con Fjango</h1>
    </body>
    </html>
    
    """)

def curriculum(request):

    doc_externo=open("./nuevotest/Plantillas/Curiculum/curriculum.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)

    return HttpResponse(documento)

def textvaribles(request):

    p1 = Persona("Estudainte Sergie", "Arizandieta")
   # temas = []
    temas = ["Plantillas","Modelos","Formularios","Vistas","Despligue"]
    #nombre = "Sergie"
    #apellido = "Arizandieta"
    fecha_actual = datetime.datetime.now()

    #doc_externo=open("./nuevotest/Plantillas/Test/index.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close()
    #documento = plt.render(ctx)

    #ctx = Context({"nombre_persona":nombre,"apellido_persona":apellido,"Fecha_actual":fecha_actual } )
    #ctx = Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"Fecha_actual":fecha_actual, "temas": temas } )
    #documento = doc_externo.render(ctx)

    #doc_externo = get_template('test.html')
    #ctx = {"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"Fecha_actual":fecha_actual, "temas": temas } 
    #documento = doc_externo.render(ctx)
   
    diccionario = {"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"Fecha_actual":fecha_actual, "temas": temas } 
    return render(request,"test.html",diccionario)

def despedida(request):

    return HttpResponse("hasta luego")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    documento = """
    <html>
    <body>
    <h1> 
    Fecha y hora actual  %s
    </h1>
    </body>
    </html>
    """ % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad,year):
    periodo = year - 2019
    edadFutura = edad + periodo
    documento = """
    <html>
    <body>
    <h1> 
    En el año %s tendras %s años 
    </h1>
    </body>
    </html>
    """ %(year, edadFutura)
    return HttpResponse(documento)