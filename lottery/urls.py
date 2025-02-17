from django.urls import path

from . import views

app_name = "lottery"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:member_id>/results/", views.results, name="results"),
    path("<int:member_id>/add_points/", views.add_points, name="add_points"),
]