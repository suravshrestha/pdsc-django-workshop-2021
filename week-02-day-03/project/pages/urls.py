from django.urls import path

from pages.views import index, about, todo, remove_todo

urlpatterns = [
    path("", index),
    path("about/", about),

    path("todos/", todo, name="todos"),
    path("remove-todo/<int:pk>/", remove_todo, name="remove_todo"),
]
