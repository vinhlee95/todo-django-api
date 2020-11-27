from django.db import models
from django.contrib.auth import get_user_model
from .base import BaseModel


class Todo(BaseModel):
  """Todo model"""
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255, blank=True)
  completed = models.BooleanField(default=False)
  completed_at = models.DateTimeField(default=None, null=True)
  completed_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None, null=True)

  def __str__(self):
    return self.title
