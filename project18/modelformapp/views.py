from django.shortcuts import render

from modelformapp.forms import StudentdetailsForm
# Create your views here.

def student_data(request):
	form=StudentdetailsForm()
	my_dict={'form':form}

	if request.method=='POST':
		form=StudentdetailsForm(request.POST)
		
		if form.is_valid():
			form.save(commit=True)
			print('Form data is stored with in the database')


	return render(request=request, template_name='modelformapp/studentform.html', context=my_dict)