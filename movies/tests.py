from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Movie


def create_movie(title='Teste', original_title='teste',
                 release_year='2000', runtime='1',
                 description='lorem ipsum', genre=['Action', 'Comedy'],
                 imdb_link='www.imdb.com', rotten_link='rottentomatoes.com',
                 imdb_rating='10', rotten_rating='10', publish=True):

    user = User.objects.create_user(username='Luiz', email='luiz@...',
                                    password='secret')

    movie = Movie.objects.create(title=title, original_title=original_title,
                                 release_year=release_year, runtime=runtime,
                                 description=description, rotten_tomatoes_rating=rotten_rating,
                                 genre=genre, rotten_tomatoes_link=rotten_link, imdb_link=imdb_link,
                                 imdb_rating=imdb_rating, publish=publish, author=user)
    return movie


class MovieViewTests(TestCase):

    def test_random_view_with_no_movies(self):

        response = self.client.get(reverse('movies:random'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nenhum filme disponível no banco de dados.")

