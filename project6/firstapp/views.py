from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_app(request):
	data='<marquee>Thanks for welcoming me Firstapp</marquee>'
	return HttpResponse(data)