from django import forms
from .models import ImageSet


class ImageForm(forms.Form):
    class Meta:
        model = ImageSet
        fields = ['image']
        images = forms.FileField(
            widget=forms.ClearableFileInput(attrs={'multiple': True}))
