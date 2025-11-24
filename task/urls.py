from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Creamos un router para manejar las URLs del ViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    # Incluye las rutas generadas automáticamente por el router (ej: /api/tasks/)
    path('', include(router.urls)),
    # Ruta para manejo de autenticación si se usa DRF simple_jwt o similar
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
]