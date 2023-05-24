from django.forms import ModelForm, TextInput
from .models import City

class WeatherForm(ModelForm):
    class Meta:
        model = City
        fields = ['location']
        widgets = {'location': TextInput(attrs={'class':'input', 'placeholder': 'Enter a Location'})}
