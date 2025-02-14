from django.contrib import admin
from django.urls import path, include

from lottery import views

urlpatterns = [
    path("polls/", include("lottery.urls")),
    path("admin/", admin.site.urls),
]