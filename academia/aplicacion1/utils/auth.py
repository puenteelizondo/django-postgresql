from django.http import JsonResponse

from users.models import usuarios

#validamos que en la tabla de usuarios este el token
def validate_token(token):
    try:
        #si esta que devuelve un tru sino un false
        usuarios.objects.get(token=token)
        return True
#cualquier exepcion que se levante cae aqui
    except Exception:
        return False