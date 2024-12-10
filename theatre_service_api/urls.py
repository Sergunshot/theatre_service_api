from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/theatre/", include("theatre.urls"), name="theatre"),
]
