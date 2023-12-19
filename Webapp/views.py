
from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona


# Create your views here.
def Bienvenido(request):
    #mensajes = {"msg1":"valor mensaje 1", "msg2":"valor mensaje 2"}
    #return render (request, "Bienvenido.html", {"msg1":"valor mensaje 1", "msg2":"valor mensaje 2"})
    no_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, "Bienvenido.html", {'Personas': personas, "no_personas": no_personas})



def Contacto(request):
    return HttpResponse("Mi nombre es Caroline Mero y mi telefono es 0993419052")
def Adios(request):
    return HttpResponse("Adios mundo desde Djand")


