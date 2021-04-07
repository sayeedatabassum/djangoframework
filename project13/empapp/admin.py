from django.contrib import admin


from empapp.models import Employeedetails
# Register your models here.
class EmployeedetailsAdmin(admin.ModelAdmin):
    
    list_display = ('name','age','address')


admin.site.register(Employeedetails, EmployeedetailsAdmin)