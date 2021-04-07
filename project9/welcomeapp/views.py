from django.shortcuts import render

import datetime
# Create your views here.

def welcome_clients(request):
	date=datetime.datetime.now()
	hour=datetime.datetime.now().hour
	msg='Hi students '

	if hour>0 and hour<12:
		msg=msg+'<h1>Good Morning</h1>'
	elif hour>12 and hour<16:
		msg=msg+'<h1>Good Afternoon</h1>'
	elif hour>16 and hour<21:
		msg=msg+'<h1>Good Evening</h1>'
	else:
		msg=msg+'Good Night'

	my_dict={'insert_date':date,'insert_msg':msg}

	return render(request=request, template_name='welcomeapp/displaygreetings.html',context=my_dict)