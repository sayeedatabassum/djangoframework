from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def bangalore_job(request):
	data='<h1>bangalore job info</h1>'
	return HttpResponse(data)

def mysore_job(request):
	data='<h1>mysore job info</h1>'
	return HttpResponse(data)

def mumbai_job(request):
	data='<h1>mumbai job info</h1>'
	return HttpResponse(data)