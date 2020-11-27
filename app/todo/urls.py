from rest_framework import routers
from django.urls import include, path
from .views import TodoViewSet

router = routers.DefaultRouter()
router.register('todos', TodoViewSet)
app_name = 'todo'

urlpatterns = [
	path('', include(router.urls))
]