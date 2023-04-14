from django.urls import path

from gestion_proyectos.proyectos_api import views

urlpatterns = [
    path('api/v1/proyecto', views.listaProyectos, name='lista_proyectos'),
    path('api/v1/proyecto/<int:id>', views.listaProyectosUsuario, name='lista_proyectos_usuario'),
    path('api/v1/proyecto', views.crearProyecto, name='crear_proyecto'),
    path('api/v1/proyecto/<int:id>', views.actualizarProyecto, name='actualizar_proyecto'),
    path('api/v1/proyecto/<int:id>', views.eliminarProyecto, name='eliminar_proyecto'),
    path('api/v1/estado', views.listaEstados, name='lista_estados'),
]
