Para instalar y probar este proyecto de manera local, siga los siguientes pasos:

## 1. Clone el repositorio desde Github usando el comando:

```git clone git@github.com:Trycatch-tv/team6-project4-backend.git```

## 2. Navegue a la carpeta del proyecto:

```cd nombre_de_repositorio```

## 3.Cree y active un entorno virtual:

```python3 -m venv myenv```
```source myenv/bin/activate```

## 4. Instale las dependencias requeridas usando pip:

```pip install -r requirements.txt```

## 5. Cree la base de datos del proyecto:

```python manage.py migrate```

## 6. Ejecute el servidor:

```python manage.py runserver```

## 7. Abra su navegador y vaya a la siguiente dirección para acceder a la página de usuarios o proyectos

```http://127.0.0.1:8000/api/v1/proyecto```
```http://127.0.0.1:8000/api/v1/usuario```



