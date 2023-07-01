from django.shortcuts import render
import json

from django.http import HttpResponse, JsonResponse

from aplicacion1.models import Clientes
from django.views.decorators.csrf import csrf_protect


def crear(request):
    # solo se permite post
    if request.method == "POST":
        # lo que hace es convertir una str a diccionario
        # la variable datos jala los datos ingresados de la base de datos
        datos = json.loads(request.body)
        Clientes.objects.create(
            name=datos["name"],
            price=datos["price"],
            category=datos["category"],
        )
        # el http es para interactuar con el frontend mensaje al ejecutar correctamente
        # agregamos el json  para devolver objetos y devolvemos los creados con un status de creados que es 201
        return JsonResponse(
            datos,
            status=201,
        )
    # cuando creas te devulve los datos con el status created
    # siempre es un 201 de created cuando todo salio bien
    else:
        # igual aca agregamos json y devovemos un mensaje junto con su status
        return JsonResponse(
            {"message": "method not allowed"},
            status=405,
        )


# si damos un get en push te va a mandar al metodo no permitido y junto con el status osea que no se puede hacer get en push
# devulve todos los obejots
def lista(request):
    # solo se permite get
    if request.method == "GET":
        # de la aplicacion traer todos los objetos de la tabla clientes
        # como ya se crea un id automatico en la base de datos solo lo que se hace es traerlo en el json
        response = [
            {
                "id": aplicacion1.id,
                "name": aplicacion1.name,
                "price": aplicacion1.price,
                "category": aplicacion1.category,
            }
            for aplicacion1 in Clientes.objects.all()
        ]
        # devolvemos en forma de diccionario los datos extraidos de response e imprimos un 200 de OK de que todo salio bien
        # bueno solo response pero agregamos otro parametro para que no de error safe=false
        return JsonResponse({"data": response}, status=200)
    else:
        # devolvemos el metodo de no encontrado porque necesitamos siempre devolver un status
        return JsonResponse(
            {"message": "method not allowed"},
            status=405,
        )


# devuleve un obejto-
# en la funcion pedimos un id de enteros
def get(request, id: int):
    # solo se permite get
    if request.method == "GET":
        try:
            # aca traemos solo un objeto con el get
            # y en el parametro le decimos que pk=id porque pk se maneja en la base de datos
            response = Clientes.objects.get(pk=id)
            # ahora solo traemos de response porque solo es uno y no todos y ahi se almacena por medio del id
            return JsonResponse(
                {
                    "id": response.id,
                    "name": response.name,
                    "price": response.price,
                    "category": response.category,
                },
                status=200,
            )
        # sino encuentra en la base de datos ya entra aqui
        except Clientes.DoesNotExist:
            # sino existe en la base de datos que devulva un mensaje que con ese id no existe
            # y el 404 es de no found
            return JsonResponse(
                {"message": f"object with {id} does not exist"}, status=404
            )
        # esta excepcion lo que hace es que cualquier otro error que ocurra exterior a el codigo entrara aqui
        except Exception:
            return JsonResponse({"message": "Internal server error"}, status=500)

    else:
        # devolvemos el metodo de no encontrado porque necesitamos siempre devolver un status
        # porque solo aceptamos gets
        return JsonResponse(
            {"message": "method not allowed"},
            status=405,
        )


# pedimos el id del item que queremos update (request)
def update(request, id: int):
    # jalamos lo que tengamos y lo metemos a la variable
    datos = json.loads(request.body)
    if request.method == "PUT":
        try:
            # aca traemos solo un objeto con el get
            # y en el parametro le decimos que pk=id porque pk se maneja en la base de datos
            # sino existe se va al 404
            object_to_update = Clientes.objects.get(pk=id)
            # ahora que ya encontro actualizamos con la variable que tiene los datos
            object_to_update.name = datos["name"]
            object_to_update.price = datos["price"]
            object_to_update.category = datos["category"]
            # cuando es item por item guardamos asi
            object_to_update.save()

            return JsonResponse(
                {
                    "id": object_to_update.id,
                    "name": object_to_update.name,
                    "price": object_to_update.price,
                    "category": object_to_update.category,
                },
                status=200,
            )
        # sino encuentra en la base de datos ya entra aqui
        except Clientes.DoesNotExist:
            # sino existe en la base de datos que devulva un mensaje que con ese id no existe
            # y el 404 es de no found
            return JsonResponse(
                {"message": f"object with {id} does not exist"}, status=404
            )
        except Exception:
            return JsonResponse({"message": "Internal server error"}, status=500)
    else:
        # devolvemos el metodo de no encontrado porque necesitamos siempre devolver un status
        # porque solo aceptamos gets
        return JsonResponse(
            {"message": "method not allowed"},
            status=405,
        )


def delete(request, id: int):
    # jalamos lo que tengamos y lo metemos a la variable
    #no usamos body porque solo lo jalamos con el id
    
    if request.method == "DELETE":
        try:
            # aca traemos solo un objeto con el get
            # y en el parametro le decimos que pk=id porque pk se maneja en la base de datos
            # sino existe se va al 404
            object_to_update = Clientes.objects.get(pk=id)
            # ahora que ya encontro borramos el objeto
            
            object_to_update.delete()

            return JsonResponse(
                {
                    "message":"object is deleted"
                },
                #se devuelve un 204 de no contend  quiere decir que se borro correctamente
                status=204,
            )
        # sino encuentra en la base de datos ya entra aqui
        except Clientes.DoesNotExist:
            # sino existe en la base de datos que devulva un mensaje que con ese id no existe
            # y el 404 es de no found
            return JsonResponse(
                {"message": f"object with {id} does not exist"}, status=404
            )
        except Exception:
            return JsonResponse({"message": "Internal server error"}, status=500)
    else:
        # devolvemos el metodo de no encontrado porque necesitamos siempre devolver un status
        # porque solo aceptamos gets
        return JsonResponse(
            {"message": "method not allowed"},
            status=405,
        )
    
