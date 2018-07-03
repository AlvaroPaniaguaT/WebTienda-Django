# WebTienda-Django

Práctica de la asignatura LTAW del Grado en Ingeniería en Sistemas Audiovisuales y Multimedia.

La práctica consiste en la creación de la parte tanto front como backend de un servicio de una tienda.

El desarrollo se ha realizado en el framework Django 1.8 para la parte del backend, para la parte frontend se ha utilizado el lenguaje de plantillas de Django, HTML5, CSS3 y JavaScript.

La aplicación hace uso de la base de datos Sqlit3 que viene configurada por defecto en Django y las tecnologías usadas en la aplicación son:

  - Formularios para la búsqueda de productos en la base de datos.
  - AJAX para la realización de peticiones asíncronas que muestran sugerencias en el formulario de búsqueda.
  - Cookies para la gestión del carro de la compra.
  - AJAX para poder hacer actualización del carro de la compra (borrar un elemento) sin tener que recargar toda la página.
  
Para ejecutar la tienda clonar todo el repositorio al equipo local y, una vez dentro nos vamos a la siguiente ruta 'TiendaDJANGO-2.0/ltawstore' , una vez dentro veremos un fichero llamado 'manage.py'. En un terminal (estando en el directorio anteriormente mencionado) ejecutamos 'python manage.py runserver 8000' lo que lanzará el servidor de la tienda.

En nuestro navegador habitual ponemos localhost:8000/ y nos llevará a la pagina de inicio.
