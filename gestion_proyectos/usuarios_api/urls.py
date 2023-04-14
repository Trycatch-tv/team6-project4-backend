from django.urls import path

import gestion_proyectos.usuarios_api.views as views

urlpatterns = [
    path('api/v1/usuario', views.listaProyectos, name='lista_usuarios', type='GET'),
    path('api/v1/usuario', views.crearUsuario, name='crear_usuario', type='POST'),
    path('api/v1/usuario/<int:id>', views.actualizarUsuario, name='actualizar_usuario', type='PUT'),
    path('api/v1/usuario/<int:id>', views.eliminarUsuario, name='eliminar_usuario', type='DELETE'),
    path('api/v1/usuario/<int:id>', views.obtenerUsuario, name='obtener_usuario', type='GET'),
]
