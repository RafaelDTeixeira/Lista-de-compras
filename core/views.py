from multiprocessing import Value
from xml.dom.minidom import Element
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import user_logged_in,get_user
from core.models import Categoria, Produto,Compra



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

def add_produtos(request):
      
    dados={
        'categorias':Categoria.objects.all(),
    }
    return render(request,'add_produtos.html',dados)

def produto_submit(request):
    produto=Produto.objects.all()
    if request.POST:
        produto=request.POST.get('produto')
        tipo=request.POST.get('categoria')
        descricao=request.POST.get('descricao')
    
    Produto.objects.update_or_create(produto=produto,
                           tipo=Categoria.objects.get(id=tipo),
                           descricao=descricao)    

    return redirect('/')

def altera_produto(request,id):

    dados={
        'produto':Produto.objects.get(id=id),
        }
    print(dados)
    return render(request,'altera_produto.html',dados)

def delete_produto(request,id):
    # Produto.objects.get(id=id).delete()
    produto={
        'produto':Produto.objects.get(id=id)
    }        
    return render(request,'produto_deletado.html',produto)
    

def deletar(request):
    id=request.POST.get('delete')
    Produto.objects.get(id=id).delete()
    return redirect('/')
   