import http

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from proyectos_api.models import Proyecto, Estado
from proyectos_api.serializer import ProyectoSerializer, EstadoSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def listaEstados(request):
    try:
        estados = Estado.objects.all()
        estados_serializer = EstadoSerializer(estados, many=True)
        return Response(estados_serializer.data, status=status.HTTP_200_OK)
    except Exception as error:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def listaProyectos(request):
    try:
        proyectos = Proyecto.objects.all()
        proyectos_serializer = ProyectoSerializer(proyectos, many=True)
        return Response(proyectos_serializer.data, status=status.HTTP_200_OK)
    except Exception as error:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def listaProyectosUsuario(request, id):
    try:
        proyectos = Proyecto.objects.filter(fk_usuario=id)
        proyectos_serializer = ProyectoSerializer(proyectos, many=True)
        return Response(proyectos_serializer.data, status=status.HTTP_200_OK)
    except Exception as error:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def crearProyecto(request):
    try:
        proyecto_data = JSONParser().parse(request)
        proyecto_serializer = ProyectoSerializer(data=proyecto_data)
        if proyecto_serializer.is_valid():
            proyecto_serializer.save()
            return JsonResponse({"mensaje": "Proyecto creado correctamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse({"mensaje": "Error al crear proyecto", "errores": proyecto_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return JsonResponse({"mensaje": "Error al crear Proyecto", "errores": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def actualizarProyecto(request, id):
    try:
        proyecto = Proyecto.objects.get(id=id)
        proyecto_data = JSONParser().parse(request)
        proyecto_serializer = ProyectoSerializer(proyecto, data=proyecto_data)
        if proyecto_serializer.is_valid():
            proyecto_serializer.save()
            return JsonResponse({"mensaje": "Proyecto actualizado correctamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse({"mensaje": "Error al actualizar proyecto", "errores": proyecto_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return JsonResponse({"mensaje": "Error al crear Proyecto", "errores": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def eliminarProyecto(request, id):
    try:
        proyecto = Proyecto.objects.get(id=id)
        proyecto.delete()
        return JsonResponse({"mensaje": "Proyecto eliminado correctamente"}, status=status.HTTP_201_CREATED)
        
    except Exception as error:
        return JsonResponse({"mensaje": "Error al crear Proyecto", "errores": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

