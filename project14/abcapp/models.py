from django.db import models

# Create your models here.
class Abcstudentdetails(models.Model):
	abcid = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	college = models.CharField(max_length=20)
	branch = models.CharField(max_length=20)
	date_of_birth = models.DateField()
	year_of_pass = models.DateField()
	percentage = models.FloatField()
	phone_number = models.CharField(max_length=50)
	mail_id = models.EmailField()

	def __str__(self):
		return self.abcid
