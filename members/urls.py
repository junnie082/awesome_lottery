from django.urls import path

from . import views

app_name = "members"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:member_id>/", views.detail, name="detail"),
    path("create_member/", views.create_member, name="create_member"),
    path("<int:member_id>/delete_member/", views.delete_member, name="delete_member"),
]