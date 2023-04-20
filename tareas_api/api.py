from tareas_api.models import Prioridad,Tamanio,Tarea,AsignacionTareas
from rest_framework import viewsets, permissions
from .serializers import PrioridadSerializer,TamanioSerializer,TareaSerializer,AsignacionTareasSerializer

class PrioridadViewSet(viewsets.ModelViewSet):
    queryset=Prioridad.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=PrioridadSerializer

class TamanioViewSet(viewsets.ModelViewSet):
    queryset=Tamanio.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=TamanioSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset=Tarea.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=TareaSerializer

class AsignacionTareasViewSet(viewsets.ModelViewSet):
    queryset=AsignacionTareas.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=AsignacionTareasSerializer