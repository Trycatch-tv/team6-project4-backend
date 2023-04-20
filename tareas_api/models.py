from django.db import models
from usuarios_api.models import Usuario
from proyectos_api.models import Estado,Proyecto

# Create your models here.
class Prioridad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=125, unique=True)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'prioridad'


class Tamanio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=125, unique=True)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tamanio'


class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=125)
    descripcion = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fk_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    fk_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fk_prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE)
    fk_tamanio = models.ForeignKey(Tamanio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tarea'
        unique_together = ('nombre', 'fk_proyecto')


class AsignacionTareas(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fk_tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.fk_tarea.nombre

    class Meta:
        db_table = 'asignar_tarea'
        unique_together = ('fk_tarea', 'fk_usuario')