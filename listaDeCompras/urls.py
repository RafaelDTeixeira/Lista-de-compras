"""listaDeCompras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from django.views import View
from core import views
from django.shortcuts import redirect, render


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('compras/',views.compras),
    path('produtos/add',views.add_produtos),
    path('produtos/submit',views.produto_submit),
    path('produto/<int:id>',views.altera_produto),
    path('produto/del/<int:id>',views.delete_produto),
    path('produto/del/submit',views.deletar)
]
