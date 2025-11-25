🚀 Overview

Este repositorio contiene la capa Backend para la aplicación Task Manager, implementada como una robusta API RESTful utilizando Django y Django REST Framework (DRF). Su principal función es gestionar la persistencia de datos (CRUD) para las tareas y manejar la autenticación de usuarios.

🛠️ Technical Stack


    Backend Framework: Python, Django, Django REST Framework (DRF)

    Database: PostgreSQL (Configurable)

    Authentication: Simple JWT (JSON Web Tokens)

    Environment: Pipenv / venv


🏗️ Architecture & Key Features


    API RESTful: Diseño de endpoints dedicados (Viewsets) para las operaciones CRUD en el modelo Task y User.

    Seguridad (Authentication): Implementación de la autenticación basada en tokens (JWT), asegurando que las peticiones al API sean stateless y seguras.

    Autorización (Permissions): Uso de permisos a nivel de objeto/usuario para garantizar que cada usuario solo pueda acceder y modificar sus propias tareas.

    Modelado de Datos: Definición de un modelo Task con relación ForeignKey al modelo de usuario, asegurando la propiedad de los datos desde la capa de la base de datos.

    Serialización: Uso de DRF Serializers para transformar los modelos de Django en respuestas JSON limpias y estructuradas.


⚙️ Endpoints Principales




Método
	Endpoint
	Descripción



POST
	/api/auth/token/
	Obtener token de acceso (login).


GET/POST
	/api/tasks/
	Listar todas las tareas del usuario / Crear nueva tarea.


GET/PUT/DEL
	/api/tasks/{id}/
	Consultar, actualizar o eliminar una tarea específica.
