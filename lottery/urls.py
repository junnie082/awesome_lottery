from django.urls import path

from . import views

app_name = "lottery"
urlpatterns = [
    path("", views.index, name="index"),
    path("entire_mem_point/<str:class_time>/<str:class_level>", views.entire_mem_point, name="entire_mem_point"),
    path("<int:member_id>/create_point/", views.create_point, name="create_point"),
    path("<int:point_id>/delete_point/", views.delete_point, name="delete_point"),
]