from django.shortcuts import render

#importing httpresponse to provide the response for the end user
from django.http import HttpResponse

# Create your views here.
def display_data(request):
	data='<h1 style="color:teal">Hi students.... welcome for learning django</h2>'
	return HttpResponse(data) 