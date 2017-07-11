from django import forms

from .models import Allergen, Item

class AllergenForm(forms.ModelForm):
    name = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'placeholder': 'Allergen Name'}))

    class Meta:
        model = Allergen
        fields = ('name',)

class AddItemForm(forms.ModelForm):
    allergens = forms.ModelMultipleChoiceField(queryset=Allergen.objects.all(), widget=forms.CheckboxSelectMultiple())
    
    class Meta:
        model = Item
        fields = ('name', 'price', 'category', 'description', 'allergens',)