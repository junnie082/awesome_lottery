from django.urls import path

from . import views

app_name = "lottery"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:member_id>/create_point/", views.create_point, name="create_point"),
    path("<int:point_id>/delete_point/", views.delete_point, name="delete_point"),
]