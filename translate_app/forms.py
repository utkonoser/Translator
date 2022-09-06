from dataclasses import fields
from django import forms
from .models import TranslateModel

class TranslateForm(forms.ModelForm):
    class Meta:
        model = TranslateModel
        fields = ['language_to_translate',
                'language_to_be_translated',
                'text_to_translate']