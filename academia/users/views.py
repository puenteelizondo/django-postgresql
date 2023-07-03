from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from users.models import usuarios
import json


#sirve para incriptar
import hashlib
# Create your views here.
#esta libreria sirve para crear tokens
import secrets
#funcione como un register
def crear(request):
    # solo se permite post
    if request.method == "POST":
        # lo que hace es convertir una str a diccionario
        # la variable datos jala los datos ingresados de la base de datos
        datos = json.loads(request.body)
        #usamos create para crearlos y almacenarlos
        usuarios.objects.create(
            email=datos["email"],
            #encriptamos el password con esta sintaxis de linea
            password=hashlib.sha512(datos["password"].encode()).hexdigest(),
            #generamos el token nosotros con esta linea, sin que el usuario tenga que escribirlo
            token=secrets.token_hex(16),
            
        )
        # el http es para interactuar con el frontend mensaje al ejecutar correctamente
        # agregamos el json  para devolver objetos y devolvemos los creados con un status de creados que es 201
        return JsonResponse(
            {
                "massage":"usuario creado con exito"
            },
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

def login(request):
    # solo se permite post
    #siempre los login son un post
    if request.method == "POST":
        
        # lo que hace es convertir una str a diccionario
        # la variable datos jala los datos ingresados de la base de datos
        datos = json.loads(request.body)
        try:
        #almacenamos en la variable para evaluar si estan en la base de datos
        #jalamos todo lo que almacena con lo que pedimos el email y password
            users = usuarios.objects.get(
            email=datos["email"],
            #encriptamos el password con esta sintaxis de linea
            password=hashlib.sha512(datos["password"].encode()).hexdigest(),
            #generamos el token nosotros con esta linea, sin que el usuario tenga que escribirlo
            
            
         )
        except usuarios.DoesNotExist:
            return JsonResponse(
                {
                    "massage":"error de usuario o contraseña"
                    #error de permisos cuando el usuario no tiene acceso a la aplicacion
                },status=401
            )
        except Exception: return JsonResponse(
                {
                    "massage":"Internal server error"
                    #error de permisos cuando el usuario no tiene acceso a la aplicacion
                },status=500)
        print(users)
        
        # el http es para interactuar con el frontend mensaje al ejecutar correctamente
        # agregamos el json  para devolver objetos y devolvemos los creados con un status de creados que es 201
        return JsonResponse(
            {
                "token":users.token
            },
            status=200,
        )
    # cuando creas te devulve los datos con el status created
    # siempre es un 201 de created cuando todo salio bien
    else:
        # igual aca agregamos json y devovemos un mensaje junto con su status
        return JsonResponse(
            {"message": "method not allowed"},
            status=405,
        )
        
def delete(request,id: int):
    # jalamos lo que tengamos y lo metemos a la variable
    #no usamos body porque solo lo jalamos con el id
    
    if request.method == "DELETE":
        try:
            # aca traemos solo un objeto con el get
            # y en el parametro le decimos que pk=id porque pk se maneja en la base de datos
            # sino existe se va al 404
            object_to_update = usuarios.objects.get(pk=id)
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
        except usuarios.DoesNotExist:
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
    
