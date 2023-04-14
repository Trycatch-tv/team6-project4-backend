import http

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from gestion_proyectos.usuarios_api.models import Usuario
from gestion_proyectos.usuarios_api.serializer import UsuarioSerializer


@api_view(['GET'])
def listaProyectos(request):
    try:
        usuarios = Usuario.objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(usuarios_serializer.data, safe=False)
    except Exception as error:
        return http.HTTPStatus.INTERNAL_SERVER_ERROR


@api_view(['POST'])
def crearUsuario(request):
    try:
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("Usuario creado correctamente", safe=False)
        return JsonResponse("Error al crear usuario", safe=False)
    except Exception as error:
        return http.HTTPStatus.INTERNAL_SERVER_ERROR


@api_view(['PUT'])
def actualizarUsuario(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(usuario, data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("Usuario actualizado correctamente", safe=False)
        return JsonResponse("Error al actualizar usuario", safe=False)
    except Exception as error:
        return http.HTTPStatus.INTERNAL_SERVER_ERROR


@api_view(['DELETE'])
def eliminarUsuario(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
        usuario.delete()
        return JsonResponse("Usuario eliminado correctamente", safe=False)
    except Exception as error:
        return http.HTTPStatus.INTERNAL_SERVER_ERROR


def obtenerUsuario(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
        usuario_serializer = UsuarioSerializer(usuario)
        return JsonResponse(usuario_serializer.data, safe=False)
    except Exception as error:
        return http.HTTPStatus.INTERNAL_SERVER_ERROR
