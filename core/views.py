from xml.dom.minidom import Element
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import user_logged_in,get_user
from core.models import Produto,Compra



def index(request):    
    lista=Produto.objects.all()  
    dados={       
        'dados':lista,
       }
    return render(request,'index.html',dados)

def compras(request):
    usuario=get_user(request)
    compras=Compra.objects.all()
    dados={
        'dados':compras,
        'usuario':usuario
    }
    return render(request,'compras.html',dados)


