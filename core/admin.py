from django.contrib import admin
from core.models import Lista

@admin.register(Lista)
class ListaAdmin(admin.ModelAdmin):
    list_display=('id','produto','preco','tipo','quantidade','descricao','mercado','usuario')
    ordering=('tipo','produto',)
