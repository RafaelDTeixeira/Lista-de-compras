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

class Produto(models.Model):
    produto=models.CharField(max_length=80)    
    tipo=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    descricao=models.TextField(null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.produto
    
class Compra(models.Model):
    produto=models.ForeignKey(Produto,on_delete=models.CASCADE)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    data=models.DateTimeField(auto_now_add=True)
    quantidade=models.IntegerField()
    mercado=models.CharField(max_length=80)
    preco=models.DecimalField(max_digits=8,decimal_places=2,verbose_name="Preco por unidade")

    def __str__(self) -> object:
        return self.produto.produto
    




     


