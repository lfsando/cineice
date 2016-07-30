from django.conf.urls import url
from django.conf.urls.static import static
from cineice import settings

from . import views


app_name = 'movies'

urlpatterns = [
    url(r'^$', views.RandomView.as_view(), name='random'),
    url(r'^filmes/generos/(?P<genre>[-\w]+)/$', views.by_genre, name='by_genre'),
    url(r'^filmes/generos/$', views.genres, name='genres_list'),
    url(r'^filmes/(?P<movie_pk>\d+)/$', views.movie_detail, name='movie_detail'),
    url(r'^filmes/novo/$', views.movie_new, name='movie_new'),
    url(r'^filmes/(?P<movie_pk>\d+)/editar/$', views.movie_edit, name='movie_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
