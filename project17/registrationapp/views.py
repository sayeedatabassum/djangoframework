from django.shortcuts import render
from registrationapp.forms import Studentform

# Create your views here.
def welcome_page(request):
	return render(request=request,template_name='registrationapp/homepage.html')

def thank_you(request):
	return render(request=request,template_name='registrationapp/thankyou.html')

def register_student(request):
	if request.method=='GET':
		form=Studentform()
		my_dict={'form':form}
		return render(request=request, template_name='registrationapp/register.html', context=my_dict)

	if request.method=='POST':
		
		form=Studentform(request.POST)
		my_dict={'form':form}

		if form.is_valid():		
			print('Data entered by the Student in the Registration Form')
			print('Name :',form.cleaned_data['name'])
			print('Password :',form.cleaned_data['password'])
			print('Re_Password :',form.cleaned_data['re_password'])
			print('Date :',form.cleaned_data['date'])
			print('ABCid :',form.cleaned_data['abcid'])
			print('PhoneNumber :',form.cleaned_data['phone_number'])
			print('Mailid :',form.cleaned_data['mailid'])
			print('Feedback :',form.cleaned_data['feedback'])

		return thank_you(request)

	return render(request=request, template_name='registrationapp/register.html', context=my_dict)




