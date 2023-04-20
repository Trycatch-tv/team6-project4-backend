from rest_framework import serializers
from usuarios_api.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','nombre','correo','clave','fecha_creacion')
        read_only_fields = ('fecha_creacion',)