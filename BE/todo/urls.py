from django.urls import path, include

from .views import ToDoView


urlpatterns = [
    path("todos/", ToDoView.as_view(), name="todos")
]


