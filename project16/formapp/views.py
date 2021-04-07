from django.shortcuts import render
from formapp.forms import Studentform
# Create your views here.

def student_form(request):
	#creation of form class object
	form=Studentform()
	my_dict={'form':form}
	return render(request=request, template_name='formapp/input.html',context=my_dict)