from django import forms
from .models import VideoList


class VideosForm(forms.ModelForm):
    class Meta:
        model = VideoList
        fields = ('name', 'body')
