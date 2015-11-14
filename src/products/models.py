from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=30) #owiuerpoajsdlfkjasd;flkiu1p3o4u134123 ewjfa;sd
	description = models.TextField()
	price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99) #100.00
	sale_price = models.DecimalField(max_digits=100,
			 decimal_places=2, default=6.99, null=True, blank=True) #100.00

	def __unicode__(self): #def __unicode__(self):
		return self.title