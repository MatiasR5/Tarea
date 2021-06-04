from typing import Text
from django.db import models

# Create your models here.

class nota(models.Model):

    nombre_nota = models.CharField ('Nombre Nota',
    max_length= 50,
    blank= False,
    null= False
    )
    descripcion_nota = models.CharField ('Descripción Nota',
    max_length= 50,
    blank= False,
    null= False
    )
    fecha_creacion = models.DateTimeField('Fecha de Creación',
    auto_now= True
    )
    fecha_finalizacion = models.DateField('Fecha de Finalización'
    )
    estado_nota = models.BooleanField(default=0)
    
    
