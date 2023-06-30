"""
URL configuration for academia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from aplicacion1 import views

# libreria para ignorar el error
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # es para que no nos de error en el post cuando hacemos un post agregamos ese error al igual que el update porque tambieen hacemos post
    path("crear/", csrf_exempt(views.crear), name="crear"),
    path("lista/", (views.lista), name="lista"),
    # cuando hagas la llamada a get/ le pidas un id
    path("get/<int:id>", (views.get), name="get"),
    path("update/<int:id>", csrf_exempt(views.update), name="update"),
    path("delete/<int:id>", (views.delete), name="delete"),
]
