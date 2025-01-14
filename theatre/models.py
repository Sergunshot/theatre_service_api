from django.db import models


class TheatreHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Play(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name="plays")
    actors = models.ManyToManyField(Actor, related_name="plays")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Performance(models.Model):
    play = models.ForeignKey(Play, related_name="performances", on_delete=models.CASCADE)
    theatre_hall = models.ForeignKey(TheatreHall, related_name="performances", on_delete=models.CASCADE)
    show_time = models.DateTimeField()
