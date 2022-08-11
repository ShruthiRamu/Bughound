from django.forms import ModelForm
from django import forms

from .program_model import Program


class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'release', 'version', 'area']

        widgets = {
            'name': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Program Name'}),
            'release': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Release'}),
            'version': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Version'}),
            'area': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Area'})
        }