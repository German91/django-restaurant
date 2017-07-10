from django import forms

from .models import Cuisine

class AddCuisineForm(forms.ModelForm):

    class Meta:
        model = Cuisine
        fields = ('name',)