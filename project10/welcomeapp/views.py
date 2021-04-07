from django.shortcuts import render

import datetime
# Create your views here.

def welcome_clients(request):
	date=datetime.datetime.now()
	hour=datetime.datetime.now().hour
	msg='Hi students '

	if hour<12:
		msg=msg+'Good Morning'
	elif hour<16:
		msg=msg+'Good Afternoon'
	elif hour>16 and hour<21:
		msg=msg+'Good Evening'
	else:
		msg=msg+'Good Night'

	my_dict={'insert_date':date,'insert_msg':msg}

	return render(request=request, template_name='welcomeapp/displaygreeting.html',context=my_dict)