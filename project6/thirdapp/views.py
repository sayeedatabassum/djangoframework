from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def third_app(request):
	data='<marquee>Thanks for making me smile no matter what thirdapp</marquee>'
	return HttpResponse(data)

