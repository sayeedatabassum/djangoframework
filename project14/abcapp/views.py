from django.shortcuts import render

from abcapp.models import Abcstudentdetails
# Create your views here.

def home_page(request):
	return render(request=request, template_name='abcapp/homepage.html')

def display_data(request):
	#Inorder to fetch the data from the database
	abc_data=Abcstudentdetails.objects.all()
	
	print(abc_data)
	print(type(abc_data))

	my_dict={'abc_data':abc_data}

	return render(request=request, template_name='abcapp/display.html',context=my_dict)