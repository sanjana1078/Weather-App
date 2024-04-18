from django import forms
from .models import WeatherData

class weatherForm(forms.ModelForm): #Forms to take data input from users
    class Meta:
        model = WeatherData
        fields=['city']