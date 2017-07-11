from django import forms

from .models import Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Category Name'}))

    class Meta:
        model = Category
        fields = ('name',)