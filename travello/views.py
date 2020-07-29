from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductosForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def home(request):
    dest = Productos.objects.all()
    contexto ={
        'dest':dest
    }
    return render(request, 'home.html', contexto)
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= username, password= password)
        if user is not None:
            auth.login(request, user)
            return redirect('login')
        else:
            messages.info(request,'Datos incorrectos')
            return redirect('login')
    else:
        return render(request,'login.html')
