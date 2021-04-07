from django.shortcuts import render

# Create your views here.
def index_page(request):
	return render(request=request, template_name='publictvapp/index.html')

def display_movie_information(request):
	main_msg = 'Latest Movie Information'
	msg1='Robert Movie will be released soon!!!!'
	msg2='KGF-2 shooting is in progress'

	my_dict={'msg1':msg1,'msg2':msg2,'main_msg':main_msg}

	return render(request=request, template_name='publictvapp/display.html',context=my_dict)


def display_sports_information(request):
	main_msg = 'Latest Sports Information'
	msg1='Hardhik Pandya hits a century'
	msg2='Virat Kohli yet to start the match '

	my_dict={'msg1':msg1,'msg2':msg2,'main_msg':main_msg}

	return render(request=request, template_name='publictvapp/display.html',context=my_dict)


def display_politics_information(request):
	main_msg = 'Latest Politics Information'
	msg1='Best bachelor of the year goes to Rahul Gandhi'
	msg2='Vatal Nagraj supports VTU students'

	my_dict={'msg1':msg1,'msg2':msg2,'main_msg':main_msg}

	return render(request=request, template_name='publictvapp/display.html',context=my_dict)