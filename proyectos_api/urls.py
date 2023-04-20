from rest_framework import routers
from .api import ProyectoViewSet, EstadoViewSet, AsignarProyectoViewSet
from tareas_api.api import PrioridadViewSet,TamanioViewSet,TareaViewSet,AsignacionTareasViewSet
from usuarios_api.api import UsuarioViewSet
router=routers.DefaultRouter()

router.register('api/Usuarios',UsuarioViewSet,'Usuarios')
router.register('api/Proyectos',ProyectoViewSet,'Proyectos')
router.register('api/Proyectos_Estado',EstadoViewSet,'Proyectos_Estado')
router.register('api/Proyectos_Asignacion',AsignarProyectoViewSet,'Proyectos_Asignacion')
router.register('api/Tarea',TareaViewSet,'Tarea')
router.register('api/Tarea_Prioridad',PrioridadViewSet,'Tarea_Prioridad')
router.register('api/Tarea_Tamanio',TamanioViewSet,'Tarea_Tamanio')
router.register('api/Tarea_Asignacion',AsignacionTareasViewSet,'Tarea_Asignacion')

urlpatterns=router.urls