from django import forms


class FindMovies(forms.Form):
    movies = forms.CharField(label='Movies', required=False)
