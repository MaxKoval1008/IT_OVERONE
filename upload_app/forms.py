from .models import Picture
from django.forms import ModelForm


class PictureForm(ModelForm):

    class Meta:
        model = Picture
        fields = '__all__'
