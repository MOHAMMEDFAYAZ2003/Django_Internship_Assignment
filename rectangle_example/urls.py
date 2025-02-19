from django.urls import path
from .views import rectangle_list, create_rectangle

urlpatterns = [
    path("", rectangle_list, name="rectangle_list"),
    path("create/", create_rectangle, name="create_rectangle"),
]
