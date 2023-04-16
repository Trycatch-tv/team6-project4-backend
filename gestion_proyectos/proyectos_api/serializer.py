from rest_framework import serializers

from proyectos_api.models import Estado, Proyecto, AsignarProyecto


class EstadoSerializer(serializers.Serializer):
    class Meta:
        model = Estado
        fields = ['id', 'nombre', 'descripcion']


class ProyectoSerializer(serializers.Serializer):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_creacion', 'fk_usuario', 'fk_estado']
    def create(self, validated_data):
        proyecto = Proyecto.objects.create(**validated_data)
        return proyecto

class AsignarProyectoSerializer(serializers.Serializer):
    class Meta:
        model = AsignarProyecto
        fields = ['id', 'fk_proyecto', 'fk_usuario']
