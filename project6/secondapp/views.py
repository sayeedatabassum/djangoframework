from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def second_app(request):
	data='<marquee>Thanks for meeting me secondapp</marquee>'
	return HttpResponse(data)

# Create your views here.
