from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

# ViewSet que maneja todas las operaciones CRUD (Create, Read, Update, Delete)
class TaskViewSet(viewsets.ModelViewSet):
    # Permite solo a usuarios autenticados acceder a esta vista
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    # Sobreescribe la función para devolver solo las tareas del usuario logueado
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    # Sobreescribe la función para guardar el usuario al crear una tarea
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
