from django.test import TestCase
from core.models.todo import Todo

class TodoModelTest(TestCase):
	"""Test case for todo model"""
	def test_model_str(self):
		"""Test creating a new todo with title"""
		title = 'Excercise'
		todo = Todo.objects.create(title=title)
		self.assertEqual(str(todo), title)