from django.urls import path
from queue_ import views

urlpatterns = [
    path("", views.index),
    path("create/", views.create),
    path("delete/<int:id>/", views.delete),
]