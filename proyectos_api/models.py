from django.db import models
from usuarios_api.models import Usuario

# Create your models here


class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=125, null=False, unique=True)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'estado'


class Proyecto(models.Model):
    nombre = models.CharField(max_length=125)
    descripcion = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fk_usuario = models.ForeignKey(
        Usuario, related_name='estados', on_delete=models.CASCADE)
    fk_estado = models.ForeignKey(Estado, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'proyecto'
        unique_together = ('nombre', 'fk_usuario')

class AsignarProyecto(models.Model):
    id = models.AutoField(primary_key=True)
    fk_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'asignar_proyecto'
        unique_together = ('fk_proyecto', 'fk_usuario')
