from django.urls import path

from . import views

app_name = "members"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:member_id>/", views.detail, name="detail"),
    path("get_create_member_form/<str:class_time>/<str:class_level>", views.get_create_member_form, name="get_create_member_form"),
    path("create_member/<str:class_time>/<str:class_level>", views.create_member, name="create_member"),
    path("<int:member_id>/delete_member/", views.delete_member, name="delete_member"),
]