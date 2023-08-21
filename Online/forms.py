from django import forms
from .models import OnlineDoctor


class OnlineDoctorForm(forms.ModelForm):
    class Meta:
        model = OnlineDoctor
        fields = ('name', 'body', 'avatar')
