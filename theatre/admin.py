from django.contrib import admin

from .models import (
    TheatreHall,
    Actor,
    Genre
)

admin.site.register(TheatreHall)
admin.site.register(Actor)
admin.site.register(Genre)
