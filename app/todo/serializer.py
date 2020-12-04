from rest_framework import serializers
from core.models.todo import Todo

class TodoSerializer(serializers.ModelSerializer):
	"""Todo serializer"""
	class Meta:
		model = Todo
		fields = ('id', 'title', 'completed')
		read_only_fields = ('id',)

	def create(self, validated_data):
		"""Create a new todo"""
		return Todo.objects.create(**validated_data)