from django.urls import path

from . import views

app_name = "dashboard"
urlpatterns = [
    path("create_dashboard/", views.create_dashboard, name="create_dashboard"),
    path("get_dashboard/<str:class_time>/<str:class_level>", views.get_dashboard, name="get_dashboard"),
]