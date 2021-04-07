from django.shortcuts import render

from django.http import HttpResponse
import datetime
# Create your views here.

#function based view

def welcome_clients(request):
	date=datetime.datetime.now()
	#the type of date is date object

	#fetch currenthour
	hour=int(datetime.datetime.now().hour)
	msg='<h1>Hi Students Good'

	if hour>0 and hour<12:
		msg=msg+'Morning'

	elif hour>12 and hour<16:
		msg=msg+'Afternoon'

	elif hour>16 and hour<21:
		msg=msg+'Evening'

	else:
		msg=msg+'Night'

	msg=msg+'</h1><hr>'

	msg=msg+'<h1> the sever time is '+str(date)+'</h1>'
	return HttpResponse(msg)