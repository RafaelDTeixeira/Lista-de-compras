from xml.dom.minidom import Element
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import user_logged_in,get_user
from core.models import Lista,Compra



def index(request):    
    lista=Lista.objects.all()  
    dados={       
        'dados':lista,
       }
    return render(request,'index.html',dados)

def compras(request):
    compras=Compra.objects.all()
    dados={
        'dados':compras,
    }
    return render(request,'compras.html',dados)


