from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("lottery/", include("lottery.urls")),
    path("admin/", admin.site.urls),
]