from django.forms import ModelForm
from .models import Cocktail
from django.forms import Form, CharField



class NewEntryForm(ModelForm):
    class Meta:
        model = Cocktail
        fields = '__all__'




