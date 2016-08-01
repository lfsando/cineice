from django import forms
from django.contrib.auth.models import User

from .models import Movie


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title', 'original_title',
                  'release_year', 'runtime',
                  'description', 'genre',
                  'imdb_link', 'imdb_rating',
                  'rotten_tomatoes_link', 'rotten_tomatoes_rating')

class NewUserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name',
			'email', 'password')