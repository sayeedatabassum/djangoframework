from django.shortcuts import render
import datetime
# Create your views here.
def welcome_clients(request):
	date=datetime.datetime.now()
	my_dict={'date':date}

	return render(request=request, template_name='timeapp/displaytime.html',context=my_dict)