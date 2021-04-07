from django import forms

class Studentform(forms.Form):
	name = forms.CharField()
	password = forms.CharField()
	re_password = forms.CharField()
	date = forms.DateField()
	abcid = forms.CharField()
	phone_number = forms.CharField()
	mailid = forms.EmailField()
	feedback = forms.CharField(widget=forms.Textarea)

