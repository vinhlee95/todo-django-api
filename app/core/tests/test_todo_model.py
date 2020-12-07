from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models.todo import Todo

class TodoModelTest(TestCase):
	"""Test case for todo model"""
	def test_model_str(self):
		"""Test creating a new todo with title"""
		title = 'Excercise'
		created_by = get_user_model().objects.create(
			username='username',
			password='password'
		)
		todo = Todo.objects.create(title=title, created_by=created_by)
		self.assertEqual(str(todo), title)