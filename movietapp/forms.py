from django import forms
from .models import moviet

class movie_form(forms.ModelForm):
    class Meta:
        model=moviet
        fields=['movie_name','movie_year','movie_duration','movie_description','movie_image']