from django import forms

from .models import Restaurant
from cuisines.models import Cuisine

class AddRestaurantForm(forms.ModelForm):
        class Meta:
            cuisine = forms.ModelChoiceField(queryset=Cuisine.objects.all())
            model = Restaurant
            fields = ('name', 'cuisine', 'phone_number', 'description', 'promotion', 'logo',)