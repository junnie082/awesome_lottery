from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("ai/", include("ai.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("lottery/", include("lottery.urls")),
    path("members/", include("members.urls")),
    path("admin/", admin.site.urls),
]