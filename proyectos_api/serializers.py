from rest_framework import serializers
from proyectos_api.models import Estado,Proyecto,AsignarProyecto

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proyecto
        fields = ('id','nombre', 'descripcion','fecha_creacion','fk_usuario','fk_estado')
        read_only_fields =('fecha_creacion',)

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estado
        fields = ('id','nombre','descripcion')

class AsignarProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model=AsignarProyecto
        fields = ('id','fk_proyecto','fk_usuario')