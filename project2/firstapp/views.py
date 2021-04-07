from django.shortcuts import render

from django.http import HttpResponse
import datetime
# Create your views here.

#function based view

def welcome_clients(request):
	date=datetime.datetime.now()
	#the type of date is date object

	msg1='<h1>welcome clients</h1>'
	msg2=msg1+'<h1>the current server time is :' +str(date) +'</h1>'

	return HttpResponse(msg2)