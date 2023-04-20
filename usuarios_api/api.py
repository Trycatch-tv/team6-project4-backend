from usuarios_api.models import Usuario
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    
    queryset=Usuario.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=UsuarioSerializer