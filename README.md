# TuEncuesta
Es una aplicacion que realiza preguntas sobre las redes sociales, demuestra en graficas la cantidad de usuarios que han realizado la encuesta y tambien las preferencias de estos.

## Estructura de la aplicacion

* `app`, es la carpeta que contiene los siguientes modulos de la aplicacion.
* `routes`, contiene las rutas de la API_Rest.
* `schemas`, tiene la clase/objeto que realiza las peticiones a la base de datos con flask_sqlalchemy.
* `static`, contiene los archivos que se usan en el front-end de la aplicacion, como: el css, los scripts y imgs.
* `templates`, en su interior tiene los archivos html que se usan para renderizar un template de las rutas, como tanto las macros que se usan en estas rutas.

### Manual de Ejecución

Primero ante todo crea la base de datos en Mysql con el nombre $sqlalchemy$.

En consola en la direccion donde guardaste la aplicacion debes de colocar:

```
py -m pip install virtualenv 
py -m virtulaenv venv
cd venv/Scripts
activate //Si no funciona prueba con ./activate
cd ../..
py -m pip install -r requirements.txt
py run.py
```
Y listo, dirigete al link http://127.0.0.1:5000

## Herramientas de Ejecución

- Python
- MySQL