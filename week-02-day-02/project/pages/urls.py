from django.urls import path

from pages.views import index, about, send, receive

urlpatterns = [
    path("", index),
    path("about/", about),
    path("send/", send),
    path("receive/", receive, name="receive"),  # Named URL
]
