from rest_framework import routers
from django.urls import path, include

from theatre.views import TheatreHallViewset

router = routers.DefaultRouter()

router.register("theatre_halls", TheatreHallViewset)

urlpatterns = [
    path("", include(router.urls)),
]
