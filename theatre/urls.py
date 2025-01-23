from rest_framework import routers
from django.urls import path, include

from theatre.views import (
    TheatreHallViewset,
    ActorViewset,
    GenreViewset,
    PlayViewset,
    PerformanceViewset,
    ReservationViewset,
)

router = routers.DefaultRouter()

router.register("theatre_halls", TheatreHallViewset)
router.register("actors", ActorViewset)
router.register("genres", GenreViewset)
router.register("plays", PlayViewset)
router.register("performances", PerformanceViewset),
router.register("reservations", ReservationViewset),

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "theatre"
