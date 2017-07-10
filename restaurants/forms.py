from django import forms

from .models import Restaurant
from cuisines.models import Cuisine

class AddRestaurantForm(forms.Form):
    name = forms.CharField(required=True, label='Restaurant Name', initial='Restaurant Name')
    cuisine = forms.ModelChoiceField(queryset=Cuisine.objects.all())
    phone_number = forms.CharField(required=True, label='Phone Number', initial='Phone Number')
    description = forms.CharField(required=False, label='Restaurant Description', initial='Restaurant description', widget=forms.Textarea)
    promotion = forms.CharField(required=False, label='Restaurant Description', initial='Restaurant description', widget=forms.Textarea)