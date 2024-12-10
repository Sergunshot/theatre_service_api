from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet

from theatre.models import TheatreHall, Actor
from theatre.serializers import TheatreHallSerializer, ActorSerializer


class TheatreHallViewset(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer


class ActorViewset(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
