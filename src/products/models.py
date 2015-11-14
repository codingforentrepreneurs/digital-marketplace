from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=30) #owiuerpoajsdlfkjasd;flkiu1p3o4u134123 ewjfa;sd

	def __unicode__(self): #def __unicode__(self):
		return self.title