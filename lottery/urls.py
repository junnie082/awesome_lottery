from django.urls import path

from . import views

app_name = "lottery"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:member_id>/add_point/", views.add_point, name="add_point"),
    path("<int:point_id>/delete_point/", views.delete_point, name="delete_point"),
]