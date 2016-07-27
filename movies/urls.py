from django.conf.urls import url

from . import views


app_name = 'movies'

urlpatterns = [
    url(r'^$', views.random_movie, name='random'),
    url(r'^movies/genres/(?P<genre>[-\w]+)/$', views.by_genre, name='by_genre'),
    url(r'^movies/genres/$', views.genres, name='genres_list'),
]
