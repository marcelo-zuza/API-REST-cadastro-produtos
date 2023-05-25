# Generated by Django 4.2.1 on 2023-05-25 14:09

import api1.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('api1', '0003_remove_produto_frete_produto_cep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='foto',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=api1.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Foto'),
        ),
    ]