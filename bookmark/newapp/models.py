from django.db import models

# Create your models here.
class Newappdetails(models.Model):
	title=models.CharField(max_length=20)
	content=models.CharField(max_length=40)

	def __str__(self):
	   return self.title


	

	
