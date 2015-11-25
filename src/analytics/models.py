from django.conf import settings
from django.db import models

# Create your models here.

from tags.models import Tag


class TagViewManager(models.Manager):
	def add_count(self, user, tag):
		obj, created = self.model.objects.get_or_create(user=user, 
			tag=tag)
		obj.count += 1
		obj.save()
		return obj


class TagView(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
	tag = models.ForeignKey(Tag)
	count = models.IntegerField(default=0)

	objects = TagViewManager()

	def __unicode__(self):
		return str(self.tag.title)