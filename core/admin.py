from django.contrib import admin
from core.models import Compra,Produto
from core.models import Categoria

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display=('id','produto','tipo','descricao')
    ordering=('tipo','produto',)
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('tipo',)
    ordering=('tipo',)

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display=('produto','quantidade','preco','usuario','mercado','data',)
    ordering=('produto',)