from django.shortcuts import render, redirect
from .models import Destination
from .forms import DestinationForm
# Create your views here.
def index(request):
    dest = Destination.objects.all()
    return render(request, 'index.html', {'dest': dest})

def listado(request):
    destinos = Destination.objects.all()
    contexto = {
    'destinos':destinos
    }
    return render(request,'listado.html', contexto)

def crear(request):
    if request.method == 'GET':
        form = DestinationForm()
        contexto ={
            'form':form
        }
    else:
        form = DestinationForm(request.POST, request.FILES)
        contexto ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('listado')
    return render(request,'crear.html', contexto)
def editar(request,id):
    destinos = Destination.objects.get(id=id)
    if request.method == 'GET':
        form = DestinationForm(instance = destinos)
        contexto ={
        'form':form
        }
    else:
        form = DestinationForm(request.POST, instance = destinos)
        contexto ={
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('listado')
    return render(request, 'crear.html', contexto)

def eliminar(request,id):
    destinos = Destination.objects.get(id=id)
    destinos.delete()

    return redirect('listado')
