from rest_framework import serializers

from gestion_proyectos.usuarios_api.models import Usuario


class UsuarioSerializer(serializers.Serializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'apellido', 'email', 'password', 'fecha_creacion', 'fk_rol')
