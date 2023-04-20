from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=125, null=False)
    correo  = models.CharField(max_length=125, null=False, unique=True)
    clave  = models.CharField(max_length=250, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'usuario'