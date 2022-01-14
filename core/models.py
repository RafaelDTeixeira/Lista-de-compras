from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Lista(models.Model):

    produto=models.CharField(max_length=80)
    quantidade=models.IntegerField()
    preco=models.DecimalField(max_digits=8,decimal_places=2)
    tipo=models.CharField(max_length=50)
    descricao=models.TextField(null=True, blank=True)
    mercado=models.CharField(max_length=80)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.produto
