from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from cineice import settings
from multiselectfield import MultiSelectField

GENRES = [
    ("Action", "Action"),
    ("Adventure", "Adventure"),
    ("Animation", "Animation"),
    ("Biography", "Biography"),
    ("Classics", "Classics"),
    ("Comedy", "Comedy"),
    ("Crime", "Crime"),
    ("Drama", "Drama"),
    ("Family", "Family"),
    ("Fantasy", "Fantasy"),
    ("Film_noir", "Film-noir"),
    ("Historical", "Historical"),
    ("Horror", "Horror"),
    ("Musical", "Musical"),
    ("Mistery", "Mistery"),
    ("Romance", "Romance"),
    ("Sci_fi", "Sci-Fi"),
    ("Sport", "Sport"),
    ("Thriller", "Thriller"),
    ("War", "War"),
    ("Western", "Western"),
]


class Movie(models.Model):
    # Movie info
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    release_year = models.IntegerField(validators=
                                       [MinValueValidator(1800),
                                        MaxValueValidator(timezone.now().year)])
    poster = models.ImageField(blank=True, upload_to='posters', default='/movies/static/movies/poster_not_available.jpg')

    runtime = models.IntegerField(blank=True, validators=[MinValueValidator(0)])
    description = models.TextField()
    genre = MultiSelectField(choices=GENRES, max_choices=4)

    # External Info
    imdb_link = models.CharField(max_length=50, default="http://www.imdb.com/search/title")
    imdb_rating = models.DecimalField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
        decimal_places=1,
        max_digits=3,
    )
    rotten_tomatoes_link = models.CharField(max_length=100, default="https://www.rottentomatoes.com/search/?search=")
    rotten_tomatoes_rating = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    # User info
    author = models.ForeignKey('auth.User')
    pub_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    user_rating = 0

    def __str__(self):
        return self.title


class Actor(models.Model):
    pass


class Director(models.Model):
    pass


class Comments(models.Model):
    pass
