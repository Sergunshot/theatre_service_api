from rest_framework import routers
from django.urls import path, include

from theatre.views import TheatreHallViewset, ActorViewset

router = routers.DefaultRouter()

router.register("theatre_halls", TheatreHallViewset)
router.register("actors", ActorViewset)

urlpatterns = [
    path("", include(router.urls)),
]
