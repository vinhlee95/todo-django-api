from rest_framework import serializers
from core.models.todo import Todo

class TodoSerializer(serializers.Serializer):
	"""Todo serializer"""
	class Meta:
		model = Todo
		fields = ('id', 'title',)
		read_only_fields = ('id',)