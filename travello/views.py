from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request,'index.html',{'dests':dests})
def listado(request):
    listado=Destination.objects.all()
    contexto= {'listado':listado}
    return render(request,'listado.html',contexto)