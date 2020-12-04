from rest_framework import serializers
from core.models.todo import Todo

class TodoSerializer(serializers.ModelSerializer):
	"""Todo serializer"""
	class Meta:
		model = Todo
		fields = ('id', 'title', 'completed')
		read_only_fields = ('id',)
