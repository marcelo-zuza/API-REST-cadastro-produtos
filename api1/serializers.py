from rest_framework import serializers
from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
                        'nome',
                        'marca',
                        'descricao',
                        'preco',
                        'foto',
                        'qte_em_estoque',
                        'criado',
                        # 'modificado'
        )
