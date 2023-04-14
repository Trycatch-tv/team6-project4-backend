from rest_framework import serializers

from gestion_proyectos.tareas_api.models import Prioridad, Tamanio, Tarea, AsignacionTareas


class PrioridadSerializer(serializers.Serializer):
    class Meta:
        model = Prioridad
        fields = ('id', 'nombre', 'descripcion')


class TamanioSerializer(serializers.Serializer):
    class Meta:
        model = Tamanio
        fields = ('id', 'nombre', 'descripcion')


class TareaSerializer(serializers.Serializer):
    class Meta:
        model = Tarea
        fields = (
            'id', 'nombre', 'descripcion', 'fecha_creacion', 'fk_estado', 'fk_proyecto', 'fk_prioridad', 'fk_tamanio')


class AsignacionTareasSerializer(serializers.Serializer):
    class Meta:
        model = AsignacionTareas
        fields = ('id', 'fecha_asignacion', 'fk_tarea', 'fk_usuario')
