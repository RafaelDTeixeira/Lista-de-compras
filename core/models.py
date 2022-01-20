from multiprocessing import Value
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
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
         return self.produto

     


