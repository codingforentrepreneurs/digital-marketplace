from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify
# Create your models here.


def download_media_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Product(models.Model):
	#user = models.OneToOneField(settings.AUTH_USER_MODEL)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	managers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="managers_products", blank=True)
	media = models.FileField(blank=True, 
			null=True, 
			upload_to=download_media_location,
			storage=FileSystemStorage(location=settings.PROTECTED_ROOT))
	title = models.CharField(max_length=30) #owiuerpoajsdlfkjasd;flkiu1p3o4u134123 ewjfa;sd
	slug = models.SlugField(blank=True, unique=True)
	description = models.TextField()
	price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99, null=True,) #100.00
	sale_price = models.DecimalField(max_digits=100,
			 decimal_places=2, default=6.99, null=True, blank=True) #100.00

	def __unicode__(self): #def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		view_name = "products:detail_slug"
		return reverse(view_name, kwargs={"slug": self.slug})



def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Product.objects.filter(slug=slug)
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug


def product_pre_save_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)
		
pre_save.connect(product_pre_save_reciever, sender=Product)




# def product_post_save_reciever(sender, instance, *args, **kwargs):
# 	if instance.slug != slugify(instance.title):
# 		instance.slug = slugify(instance.title)
# 		instance.save()

# post_save.connect(product_post_save_reciever, sender=Product)