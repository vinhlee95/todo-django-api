from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from core.models.todo import Todo
from todo.serializer import TodoSerializer

from core.tests.authenticated_test_case import AuthenticatedTestCase

TODO_URL = '/api/todos/'

def get_detail_url(id):
	"""Get URL for todo detail view"""
	return f'{TODO_URL}{id}'

def mock_todo(title='Mocked todo', **args):
	"""Mock a todo object and save it to db"""
	return Todo.objects.create(title=title, **args)

class PublicTodoApiTest(TestCase):
	"""Test for public Todo API"""
	def setUp(self):
		"""Setup that run before the test case"""
		self.client = APIClient()

	def test_authentication(self):
		"""Test server throws error when client is unauthenticated"""
		client = APIClient()
		res = client.get(TODO_URL)
		self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class TodoApiTest(AuthenticatedTestCase):
	"""Tests for Todo API"""

	def setUp(self):
		"""Setup that run before the test case"""
		super().setUp()

	def test_retrieve_todos(self):
		"""Test if we can get all todos in db"""
		mock_todo()
		mock_todo()
		res = self.client.get(TODO_URL)

		serializer = TodoSerializer(Todo.objects.all(), many=True)

		# Assertions
		self.assertEqual(res.status_code, status.HTTP_200_OK)
		self.assertEqual(res.data, serializer.data)

	def test_create_todo(self):
		"""Test if we can create a new todo"""
		payload = {'title': 'Go to school', 'completed': False}
		res = self.client.post(TODO_URL, payload)
		serializer = TodoSerializer(Todo.objects.get(id=res.data['id']))

		# Assertions
		self.assertEqual(res.status_code, status.HTTP_201_CREATED)
		self.assertEqual(res.data, serializer.data)

	def test_create_invalid_todo(self):
		"""Test if the server throws 400 when request data is invalid"""
		payload = {'completed': False}
		res = self.client.post(TODO_URL, payload)

		self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

	def test_update_todo(self):
		"""Test if we can update the todo"""
		mocked_todo_payload = {
			'title': 'Do laundry',
			'completed': False
		}
		mocked_todo = mock_todo(**mocked_todo_payload)
		update_todo_payload = {
			'title': 'Skip laundry',
			'completed': True
		}
		res = self.client.put(get_detail_url(mocked_todo.id), update_todo_payload)

		# Assertions
		self.assertEqual(res.status_code, status.HTTP_200_OK)
		self.assertEqual(res.data['title'], update_todo_payload['title'])
		self.assertEqual(res.data['completed'], update_todo_payload['completed'])

	def test_delete_todo(self):
		"""Test if we can delete a todo"""
		todo = mock_todo()
		res = self.client.delete(get_detail_url(todo.id))

		self.assertEqual(res.status_code, status.HTTP_200_OK)
		with self.assertRaises(Exception):
			Todo.objects.get(id=todo.id)

	def test_completed_todo(self):
		"""Test if a todo is completed by an user"""
		todo = mock_todo()
		payload = {'completed': True}
		res = self.client.patch(get_detail_url(todo.id), payload)

		# Assertions
		self.assertEqual(res.status_code, status.HTTP_200_OK)
		self.assertEqual(res.data['completed'], True)
		self.assertEqual(res.data['completed_by'], self.user.id)
		self.assertIn('completed_at', res.data)


