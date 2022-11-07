from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader
from MVT.models import *


def fecha(request):
    hoy = datetime.now()
    saludo_con_fecha = f"Hola Coder! hoy es {hoy.date()} y son las {hoy.time()}"
    return(HttpResponse(saludo_con_fecha))

def inicio(request):
    plantilla = loader.get_template("inicio.html")
    lstFamiliares = Familiar.objects.all()
    familiar = {"lstFamiliares": lstFamiliares}
    documento = plantilla.render(familiar)
    return(HttpResponse(documento))
    