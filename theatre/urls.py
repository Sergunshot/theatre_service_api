from rest_framework import routers
from django.urls import path, include

from theatre.views import (
    TheatreHallViewset,
    ActorViewset,
    GenreViewset
)

router = routers.DefaultRouter()

router.register("theatre_halls", TheatreHallViewset)
router.register("actors", ActorViewset)
router.register("genres", GenreViewset)

urlpatterns = [
    path("", include(router.urls)),
]
