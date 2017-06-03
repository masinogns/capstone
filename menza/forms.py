from django import forms
from .models import Photo

class UploadForm(forms.ModelForm):

    comment = forms.CharField(max_length=255)

    class Meta:
        model = Photo
        exclude = ('thumnail_image', 'owner')
