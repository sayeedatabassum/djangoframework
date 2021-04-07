from django import forms

from modelformapp.models import Studentdetails

class StudentdetailsForm(forms.ModelForm):
    # TODO: Define form fields here
    class Meta:
    	model=Studentdetails
    	fields='__all__'