from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

class AuthenticatedTestCase(TestCase):
  """
  Setup for authenticated test cases
  - Init API client
  - Mock and authenticate user
  """
  def setUp(self):
    """Set up"""
    self.client = APIClient()
    self.user = self.mock_user()
    self.client.force_authenticate(user=self.user)

  def mock_user(self):
    """Mock a user"""
    return get_user_model().objects.create(
      username = "test_username",
      password = "password"
    )
