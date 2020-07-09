from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request,'index.html',{'dests':dests})
def listado(request):
    destinos = Destination.objects.all()
    contexto  = {
        'destinos':destinos
    }
    return render(request,'listado.html',contexto)