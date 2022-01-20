from django.contrib import admin
from core.models import Lista
from core.models import Categoria

@admin.register(Lista)
class ListaAdmin(admin.ModelAdmin):
    list_display=('id','produto','preco','tipo','quantidade','descricao','mercado','usuario')
    ordering=('tipo','produto',)
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('tipo',)
    ordering=('tipo',)
    