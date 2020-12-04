from rest_framework import routers
from django.urls import include, path
from .views import CrateTodoView

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
	path('', CrateTodoView.as_view(), name='create')
]
