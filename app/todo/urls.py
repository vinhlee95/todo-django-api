from rest_framework import routers
from django.urls import include, path
from .views import TodoView

# Router implementation
# ONLY used with a viewset
# router = routers.DefaultRouter()
# router.register('todos', TodoViewSet)
#
# urlpatterns = [
# 	path('', include(router.urls))
# ]

app_name = 'todo'

urlpatterns = [
	path('', TodoView.as_view()),
	path('<int:pk>', TodoView.as_view())
]
