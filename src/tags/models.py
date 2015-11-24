from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify

# Create your models here.

from products.models import Product

class TagQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)


class TagManager(models.Manager):
	def get_queryset(self):
		return TagQuerySet(self.model, using=self._db)

	def all(self, *args, **kwargs):
		return super(TagManager, self).all(*args, **kwargs).active()


class Tag(models.Model):
	title = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(unique=True)
	products = models.ManyToManyField(Product, blank=True)
	active = models.BooleanField(default=True)

	objects = TagManager()

	def __unicode__(self):
		return str(self.title)

	def get_absolute_url(self):
		view_name = "tags:detail"
		return reverse(view_name, kwargs={"slug": self.slug})



def tag_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.title = instance.title.lower()
	if not instance.slug:
		instance.slug = slugify(instance.title)
		
pre_save.connect(tag_pre_save_receiver, sender=Tag)