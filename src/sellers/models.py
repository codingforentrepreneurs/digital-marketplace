from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.


class SellerAccount(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	managers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="manager_sellers", blank=True)
	active = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


	def __unicode__(self):
		return str(self.user.username)

	def get_absolute_url(self):
		return reverse("products:vendor_detail", kwargs={"vendor_name": self.user.username})
