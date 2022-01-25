from datetime import datetime
from msilib.schema import Class
from multiprocessing import Value
from unicodedata import decimal
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Categoria(models.Model):
    tipo=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.tipo

class Lista(models.Model):
    produto=models.CharField(max_length=80)
    quantidade=models.IntegerField()
    preco=models.DecimalField(max_digits=8,decimal_places=2,verbose_name="Preco por unidade")
    tipo=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    descricao=models.TextField(null=True, blank=True)
    mercado=models.CharField(max_length=80)
    
    def __str__(self) -> str:
        return self.produto
    
class Compra(models.Model):
    produto=models.ForeignKey(Lista,on_delete=models.CASCADE)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    data=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> object:
        return self.produto.produto
    




     


