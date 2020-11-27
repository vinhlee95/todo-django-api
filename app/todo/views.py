from rest_framework import viewsets
from core.models.todo import Todo
from .serializer import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
	"""Todo viewset"""
	serializer_class = TodoSerializer
	queryset = Todo.objects.all()