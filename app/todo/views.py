from rest_framework import viewsets, generics, mixins, \
													views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone

from core.models.todo import Todo
from .serializer import TodoSerializer

# Viewset 1-size-fit-all implementation
# class TodoViewSet(generics.CreateAPIView):
# 	"""Todo viewset"""
# 	serializer_class = TodoSerializer
# 	permission_classes = (IsAuthenticated,)
# 	queryset = Todo.objects.all()

class ListTodoView(views.APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		"""Todo view for listing all todos"""
		todos = Todo.objects.all()
		serializer = TodoSerializer(todos, many=True)
		return Response(serializer.data)

	def post(self, request):
		"""Create a new todo"""
		serializer = TodoSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			saved_todo = serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class TodoView(views.APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, pk):
		"""Todo view for retrieving a todo"""
		todo = get_object_or_404(Todo, id=pk)
		serializer = TodoSerializer(instance=todo)
		return Response(serializer.data)

	def put(self, request, pk):
		"""Update a todo"""
		saved_todo = get_object_or_404(Todo, id=pk)
		serializer = TodoSerializer(instance=saved_todo, data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
		return Response(serializer.data)

	def patch(self, request, pk):
		"""Partially update a todo"""
		saved_todo = get_object_or_404(Todo, id=pk)
		serializer = TodoSerializer(instance=saved_todo, data=request.data, partial=True)
		if serializer.is_valid(raise_exception=True):
			if request.data['completed']:
				serializer.save(completed_by=request.user, completed_at=timezone.now())
			else:
				serializer.save()
		return Response(serializer.data)

	def delete(self, request, pk):
		"""Delete a todo"""
		todo = get_object_or_404(Todo, id=pk)
		todo.delete()
		return Response({'message': 'success'})



