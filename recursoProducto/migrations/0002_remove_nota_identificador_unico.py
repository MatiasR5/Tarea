# Generated by Django 3.2.4 on 2021-06-04 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recursoProducto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='identificador_unico',
        ),
    ]
