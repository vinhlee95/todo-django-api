from rest_framework import serializers
from core.models import Todo

class TodoSerializer(serializers.ModelSerializer):
	"""Todo serializer"""
	class Meta:
		model = Todo
		fields = ('id', 'title', 'completed', 'completed_by', 'completed_at')
		read_only_fields = ('id',)

