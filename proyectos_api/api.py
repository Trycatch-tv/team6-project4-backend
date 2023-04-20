from proyectos_api.models import Proyecto, Estado, AsignarProyecto
from rest_framework import viewsets, permissions
from .serializers import ProyectoSerializer, EstadoSerializer, AsignarProyectoSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset=Proyecto.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ProyectoSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset=Estado.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=EstadoSerializer

class AsignarProyectoViewSet(viewsets.ModelViewSet):
    queryset=AsignarProyecto.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=AsignarProyectoSerializer