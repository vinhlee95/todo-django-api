from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from core.models.todo import Todo
from todo.serializer import TodoSerializer

TODO_URL = reverse('todo:todo-list')

def mock_todo(title='Mocked todo', **args):
	"""Mock a todo object and save it to db"""
	return Todo.objects.create(title=title, **args)

class TodoApiTest(TestCase):
	"""Tests for Todo API"""

	def setUp(self):
		"""Setup that run before the test case"""
		self.client = APIClient()

	def test_retrieve_todos(self):
		"""Test if we can get all todos in db"""
		mock_todo()
		mock_todo()
		res = self.client.get(TODO_URL)

		serializer = TodoSerializer(Todo.objects.all(), many=True)
		print(serializer.data)

		# Assertions
		self.assertEqual(res.status_code, status.HTTP_200_OK)
		self.assertEqual(res.data, serializer.data)

