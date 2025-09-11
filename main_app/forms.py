from django import forms
from .models import Play


class PlayForm(forms.ModelForm):
  class Meta:
    model = Play
    fields = ['date', 'note']
    widgets = {
      'date': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={
          'placeholder': 'Select a date',
          'type': 'date'
        }
      ),
    }