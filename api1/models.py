from django.db import models
from stdimage import StdImageField
import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    marca = models.CharField('Marca', max_length=100)
    descricao = models.TextField('Descrição', max_length=700)
    preco = models.DecimalField('Preço', decimal_places=2, max_length=10, max_digits=10)
    foto = StdImageField(
        'Foto', upload_to=get_file_path,
        variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}
    )
    cep = models.CharField('Cep', max_length=8, default='')
    qte_em_estoque = models.IntegerField('Quantidade_em_estoque',max_length=4, default=0)

    def calcula_frete(self):
        custo_frete = 0
        if self.cep[0] == '1':
            custo_frete = (self.preco * 5) / 100
        elif self.cep[0] == '2':
            custo_frete = (self.preco * 10) / 100
        elif self.cep[0] == '3':
            custo_frete = (self.preco * 15) / 100
        else:
            custo_frete = 0
        return custo_frete

    def __str__(self):
        return self.nome
