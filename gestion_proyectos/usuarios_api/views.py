import http
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response

from usuarios_api.models import Usuario
from usuarios_api.serializer import UsuarioSerializer


@api_view(['GET'])
def lista_usuarios(request):
    try:
        usuarios = Usuario.objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        return Response(usuarios_serializer.data, status=status.HTTP_200_OK)
    except Exception as error:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def crearUsuario(request):
    try:
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse({"mensaje": "Usuario creado correctamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse({"mensaje": "Error al crear usuario", "errores": usuario_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return JsonResponse({"mensaje": "Error al crear usuario", "errores": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
