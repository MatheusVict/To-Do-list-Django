from django import forms
from .models import task

class taskform(forms.ModelForm):

    class Meta:
        model = task
        fields = ('title', 'description')