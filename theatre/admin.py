from django.contrib import admin

from .models import (
    TheatreHall,
    Actor,
    Genre,
    Play
)

admin.site.register(TheatreHall)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Play)
