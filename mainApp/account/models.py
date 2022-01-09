from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
	SEX = (
			('Erkek', 'Erkek'),
			('Kadın', 'Kadın'),
			) 
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	tckn = models.CharField(max_length=11,null=True)
	name = models.CharField(max_length=200, null=True)
	surname = models.CharField(max_length=200, null=True)
	age = models.IntegerField(null=True)
	sex = models.CharField(max_length=200, choices=SEX)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	img = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name
        