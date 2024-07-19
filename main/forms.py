from django import forms
from .models import Leed


class GoLead(forms.ModelForm):
    class Meta:
        model = Leed
        fields = '__all__'
