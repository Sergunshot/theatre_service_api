from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from theatre.models import Play, Genre, Actor, TheatreHall, Performance
from theatre.serializers import PlayListSerializer

PLAY_URL = reverse("theatre:play-list")


def sample_genre(**params):
    defaults = {
        "name": "Drama",
    }
    defaults.update(params)

    return Genre.objects.create(**defaults)


def sample_actor(**params):
    defaults = {"first_name": "George", "last_name": "Clooney"}
    defaults.update(params)

    return Actor.objects.create(**defaults)


def sample_play(**params):
    defaults = {
        "title": "Sample play",
        "description": "Sample description",
        "duration": 90,
    }
    defaults.update(params)

    return Play.objects.create(**defaults)


def sample_performance(**params):
    theatre_hall = TheatreHall.objects.create(name="Blue", rows=20, seats_in_row=20)

    defaults = {
        "show_time": "2022-06-02 14:00:00",
        "play": None,
        "cinema_hall": theatre_hall,
    }
    defaults.update(params)

    return Performance.objects.create(**defaults)


class UnauthenticatedMovieAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(PLAY_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedMovieAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="test@test.com", password="testpassword"
        )
        self.client.force_authenticate(self.user)

    def test_play_list(self):
        sample_play()
        res = self.client.get(PLAY_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        plays = Play.objects.all()
        serializer = PlayListSerializer(plays, many=True)
        self.assertEqual(res.data["results"], serializer.data)

    def test_movies_by_actors(self):
        play = sample_play()
        play_first = sample_play(title="First play")
        play_second = sample_play(title="Second play")
        actor_1 = sample_actor(first_name="John", last_name="Doe")
        actor_2 = sample_actor(first_name="Jane", last_name="Doe")
        play_first.actors.add(actor_1)
        play_second.actors.add(actor_2)
        res = self.client.get(PLAY_URL, {"actors": f"{actor_1.id},{actor_2.id}"})
        play_first_serializer = PlayListSerializer(play_first)
        play_second_serializer = PlayListSerializer(play_second)
        play_serializer = PlayListSerializer(play)
        self.assertIn(play_first_serializer.data, res.data["results"])
        self.assertIn(play_second_serializer.data, res.data["results"])
        self.assertNotIn(play_serializer.data, res.data["results"])

    def test_movies_by_genres(self):
        play = sample_play()
        play_first = sample_play(title="First play")
        play_second = sample_play(title="Second play")
        genre_1 = sample_genre(name="Horror")
        genre_2 = sample_genre(name="Adventure")
        play_first.genres.add(genre_1)
        play_second.genres.add(genre_2)
        res = self.client.get(PLAY_URL, {"genres": f"{genre_1.id},{genre_2.id}"})
        play_first_serializer = PlayListSerializer(play_first)
        play_second_serializer = PlayListSerializer(play_second)
        play_serializer = PlayListSerializer(play)
        self.assertIn(play_first_serializer.data, res.data["results"])
        self.assertIn(play_second_serializer.data, res.data["results"])
        self.assertNotIn(play_serializer.data, res.data["results"])
