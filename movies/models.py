from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from cineice import settings
import os
from multiselectfield import MultiSelectField

GENRES = [
    ("acao", "Ação"),
    ("aventura", "Aventura"),
    ("animacao", "Animação"),
    ("biografico", "Biográfico"),
    ("classicos", "Classicos"),
    ("comedia", "Comédia"),
    ("crime", "Crime"),
    ("drama", "Drama"),
    ("familia", "Família"),
    ("fantasia", "Fantasia"),
    ("filme_noir", "Film-noir"),
    ("historico", "Histórico"),
    ("terror", "Terror"),
    ("musical", "Musical"),
    ("misterio", "Mistério"),
    ("romance", "Romance"),
    ("ficcao_cientifica", "Ficção Científica"),
    ("esporte", "Esporte"),
    ("suspense", "Suspense"),
    ("guerra", "Guerra"),
    ("western", "Western"),
]


class Movie(models.Model):
    # Movie info
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    release_year = models.IntegerField(validators=
                                       [MinValueValidator(1800),
                                        MaxValueValidator(timezone.now().year)])
    poster = models.ImageField(blank=True, upload_to='posters',
                               default='poster_not_available.jpg')

    runtime = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()
    genre = MultiSelectField(choices=GENRES, max_choices=4)

    # External Info
    imdb_link = models.CharField(max_length=50)
    imdb_rating = models.DecimalField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
        decimal_places=1,
        max_digits=3,
    )
    rotten_tomatoes_link = models.CharField(max_length=100)
    rotten_tomatoes_rating = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    # Other infos
    publish = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User')
    pub_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    user_rating = 0

    def publish_movie(self, publish=True):
        self.publish = publish

    def __str__(self):
        return self.title


class Actor(models.Model):
    pass


class Director(models.Model):
    pass


class Comments(models.Model):
    pass
