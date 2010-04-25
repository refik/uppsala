from django import forms
from uppsala.fileshare.models import UploadedFile

class UploadFileForm(forms.Form):
    file  = forms.FileField()
