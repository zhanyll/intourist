from django import forms
from .models import Place, Feedback


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'location', 'decription']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['place', 'text']