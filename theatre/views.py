from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet

from theatre.models import TheatreHall
from theatre.serializers import TheatreHallSerializer


class TheatreHallViewset(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer
