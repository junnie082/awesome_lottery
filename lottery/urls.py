from django.urls import path

from . import views

app_name = "lottery"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:member_id>/", views.detail, name="detail"),
    path("<int:member_id>/results/", views.results, name="results"),
    path("<int:member_id>/vote/", views.vote, name="vote"),
    path("create_member_form/", views.create_member_form, name="create_member_form"),
    path("<int:member_id>/add_points/", views.add_points, name="add_points"),
]