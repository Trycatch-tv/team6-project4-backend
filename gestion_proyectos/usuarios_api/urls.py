from django.urls import path

import usuarios_api.views as views

urlpatterns = [
    path('api/v1/usuario', views.lista_usuarios, name='lista_usuarios'),
    path('api/v1/usuario/crear', views.crearUsuario, name='crear_usuario'),
    path('api/v1/usuario/<int:id>', views.actualizarUsuario, name='actualizar_usuario'),
    path('api/v1/usuario/<int:id>', views.eliminarUsuario, name='eliminar_usuario'),
    path('api/v1/usuario/<int:id>', views.obtenerUsuario, name='obtener_usuario'),
]
