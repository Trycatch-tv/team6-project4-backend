from rest_framework import serializers
from tareas_api.models import Prioridad, Tamanio, Tarea, AsignacionTareas


class PrioridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prioridad
        fields = ('id','nombre','descripcion')
        read_only_fields = ('fecha_creacion',)


class TamanioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tamanio
        fields = ('id','nombre','descripcion')
        read_only_fields = ('fecha_creacion',)


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ('id','nombre','descripcion','fecha_creacion','fk_estado','fk_proyecto','fk_prioridad','fk_tamanio')
        read_only_fields = ('fecha_creacion',)


class AsignacionTareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionTareas
        fields = ('id','fecha_asignacion','fk_tarea','fk_usuario')
        read_only_fields = ('fecha_asignacion',)
