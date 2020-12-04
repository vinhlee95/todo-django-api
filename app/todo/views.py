from rest_framework import viewsets, generics, mixins, \
													views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
