from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome',
                    'marca',
                    'descricao',
                    'preco',
                    'foto',
                    'cep',
                    'qte_em_estoque',
                    'criado',
                    'modificado')
