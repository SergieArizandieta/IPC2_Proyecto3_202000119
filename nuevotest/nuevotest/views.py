from django.http import HttpRequest
from django.http.response import HttpResponse

def saludo(request):

    return HttpResponse("Hola alumnos esta es nuestra primer pagina con Django")