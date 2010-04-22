from django import forms

class newMeet(forms.Form):
	place = forms.CharField()
	date = forms.DateField(widget=forms.DateInput)
