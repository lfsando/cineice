from django.contrib import admin
from movies.models import Movie


class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Movie informations',              {'fields': ['title', 'original_title',
                                                        'release_year', 'poster',
                                                        'runtime', 'genre',
                                                        'description']}),

        ('External links and information',  {'fields': ['imdb_link', 'imdb_rating',
                                                        'rotten_tomatoes_link', 'rotten_tomatoes_rating']}),

        ('Other informations',                {'fields': ['author', 'pub_date', 'publish']}),
    ]
    list_display = ('title', 'release_year', 'author', 'publish')
    list_filter = ('release_year', 'publish')
    search_fields = ['title', 'original_title', 'release_year']


admin.site.register(Movie, MovieAdmin)
