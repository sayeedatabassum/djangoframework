from django.shortcuts import render

# Create your views here.
def welcome_clients(request):
	return render(request=request, template_name='greetingapp/display.html')