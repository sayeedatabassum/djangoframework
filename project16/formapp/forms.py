from django import forms

class Studentform(forms.Form):
    # TODO: Define form fields here

	name = forms.CharField()
	age = forms.IntegerField()
	address = forms.CharField()

	