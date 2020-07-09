from django.shortcuts import render, redirect
from .models import Destination
from .forms import DestinationForm
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
def crear(request):
    if request.method=='GET':
        form = DestinationForm()
        contexto = {
            'form':form
        }
    else:
        form = DestinationForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('listado')
    return render(request,'crear.html',contexto)