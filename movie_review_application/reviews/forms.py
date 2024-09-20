from django import forms
from .models import Review, Movie


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'rating', 'comment']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}, choices=[(i, i) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'release_year']