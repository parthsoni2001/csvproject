from django import forms
from .models import UploadCSV



class UploadCSVForm(forms.ModelForm):

    class Meta:
        model = UploadCSV
        fields = ['upload']