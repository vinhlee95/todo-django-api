from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from core.models.todo import Todo
from .serializer import TodoSerializer

# class TodoViewSet(generics.CreateAPIView):
# 	"""Todo viewset"""
# 	serializer_class = TodoSerializer
# 	permission_classes = (IsAuthenticated,)
# 	queryset = Todo.objects.all()

class CrateTodoView(generics.CreateAPIView):
	"""Create Todo view"""
	serializer_class = TodoSerializer
	permission_classes = (IsAuthenticated,)
