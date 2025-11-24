from rest_framework import serializers
from .models import Task

# Serializer para convertir la instancia de Task de Python a JSON (y viceversa)
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # Campos que se expondrán en la API
        fields = ['id', 'user', 'title', 'description', 'completed', 'created_at']
        read_only_fields = ['user'] # El usuario se asigna en la vista, no en el cliente