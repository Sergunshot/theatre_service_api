from rest_framework import routers
from django.urls import path, include

from theatre.views import (
    TheatreHallViewSet,
    ActorViewSet,
    GenreViewSet,
    PlayViewSet,
    PerformanceViewSet,
    ReservationViewSet,
)

router = routers.DefaultRouter()

router.register("theatre_halls", TheatreHallViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("plays", PlayViewSet)
router.register("performances", PerformanceViewSet),
router.register("reservations", ReservationViewSet),

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "theatre"
