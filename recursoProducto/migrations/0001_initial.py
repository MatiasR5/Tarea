# Generated by Django 3.2.4 on 2021-06-04 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador_unico', models.IntegerField(verbose_name='ID')),
                ('nombre_nota', models.CharField(max_length=50, verbose_name='Nombre Nota')),
                ('descripcion_nota', models.CharField(max_length=50, verbose_name='Descripción Nota')),
                ('fecha_creacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Creación')),
                ('fecha_finalizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Finalización')),
                ('estado_nota', models.BooleanField(default=0)),
            ],
        ),
    ]
