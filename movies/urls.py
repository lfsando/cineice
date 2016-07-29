from django.conf.urls import url
from django.conf.urls.static import static
from cineice import settings

from . import views


app_name = 'movies'

urlpatterns = [
    url(r'^$', views.RandomView.as_view(), name='random'),
    url(r'^movies/genres/(?P<genre>[-\w]+)/$', views.by_genre, name='by_genre'),
    url(r'^movies/genres/$', views.genres, name='genres_list'),
    url(r'^movies/(?P<movie_pk>\d+)/$', views.movie_detail, name='movie_detail'),
    url(r'^movies/new/$', views.movie_new, name='movie_new'),
    url(r'^movies/(?P<movie_pk>\d+)/edit/$', views.movie_edit, name='movie_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
