from django.conf import settings
from django.db import models

# Create your models here.

from tags.models import Tag


class TagView(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
	tag = models.ForeignKey(Tag)
	count = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.tag.title)