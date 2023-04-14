import http

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from gestion_proyectos.proyectos_api.models import Proyecto, Estado
from gestion_proyectos.proyectos_api.serializer import ProyectoSerializer, EstadoSerializer


@api_view(['GET'])
def listaEstados(request):
    try:
        estados = Estado.objects.all()
        estados_serializer = EstadoSerializer(estados, many=True)
        return JsonResponse(estados_serializer.data, safe=False)
    except Exception as error:
        return http.HTTPStatus.INTERNAL_SERVER_ERROR


@api_view(['GET'])
def listaProyectos(request):
    try:
        proyectos = Proyecto.objects.all()
        proyectos_serializer = ProyectoSerializer(proyectos, many=True)
        return JsonResponse(proyectos_serializer.data, safe=False)
    except Exception as error:
        return http.HTTPStatus.INTERNAL_SERVER_ERROR


@api_view(['GET'])
def listaProyectosUsuario(request, id):
    try:
        proyectos = Proyecto.objects.filter(fk_usuario=id)
        proyectos_serializer = ProyectoSerializer(proyectos, many=True)
        return JsonResponse(proyectos_serializer.data, safe=False)
    except Exception as error:
        return http.HTTPStatus.INTERNAL_SERVER_ERROR


@api_view(['POST'])
def crearProyecto(request):
    try:
        proyecto_data = JSONParser().parse(request)
        proyecto_serializer = ProyectoSerializer(data=proyecto_data)
        if proyecto_serializer.is_valid():
            proyecto_serializer.save()
            return JsonResponse("Proyecto creado correctamente", safe=False)
        return JsonResponse("Error al crear proyecto", safe=False)
    except Exception as error:
        return http.HTTPStatus.INTERNAL_SERVER_ERROR


@api_view(['PUT'])
def actualizarProyecto(request, id):
    try:
        proyecto = Proyecto.objects.get(id=id)
        proyecto_data = JSONParser().parse(request)
        proyecto_serializer = ProyectoSerializer(proyecto, data=proyecto_data)
        if proyecto_serializer.is_valid():
            proyecto_serializer.save()
            return JsonResponse("Proyecto actualizado correctamente", safe=False)
        return JsonResponse("Error al actualizar proyecto", safe=False)
    except Exception as error:
        return http.HTTPStatus.INTERNAL_SERVER_ERROR


@api_view(['DELETE'])
def eliminarProyecto(request, id):
    try:
        proyecto = Proyecto.objects.get(id=id)
        proyecto.delete()
        return JsonResponse("Proyecto eliminado correctamente", safe=False)
    except Exception as error:
        return http.HTTPStatus.INTERNAL_SERVER_ERROR
