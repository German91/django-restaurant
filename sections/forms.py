from django import forms

from .models import Section

class SectionForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Section Name'}))
    class Meta:
        model = Section
        fields = ('name',)