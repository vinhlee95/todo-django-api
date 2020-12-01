from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.models.todo import Todo
from .serializer import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
	"""Todo viewset"""
	serializer_class = TodoSerializer
	permission_classes = (IsAuthenticated,)
	queryset = Todo.objects.all()
