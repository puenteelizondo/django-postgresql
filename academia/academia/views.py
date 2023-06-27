from django.http import HttpResponse

#primera vista
def saludo(request):

    #devolvernos una respuesta
    return HttpResponse("Hola chavales esta es mi primera conexion usando API Django para Base de datos uwu")
def despedida(request):

    #devolvernos una respuesta
    return HttpResponse("Son 1000 pesos joven")