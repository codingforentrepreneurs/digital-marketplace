from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify
# Create your models here.




def download_media_location(instance, filename):
	return "%s/%s" %(instance.slug, filename)

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

	def get_download(self):
		view_name = "products:download_slug"
		url = reverse(view_name, kwargs={"slug": self.slug})
		return url



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



def thumbnail_location(instance, filename):
	return "%s/%s" %(instance.product.slug, filename)


class Thumbnail(models.Model):
	product = models.ForeignKey(Product)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	height = models.CharField(max_length=20, null=True, blank=True)
	width = models.CharField(max_length=20, null=True, blank=True) 
	media = models.ImageField(
		width_field = "width",
		height_field = "height",
		blank=True, 
		null=True, 
		upload_to=thumbnail_location)

	def __unicode__(self): # __str__(self):
		return str(self.media.path)





class MyProducts(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	products = models.ManyToManyField(Product, blank=True)


	def __unicode__(self):
		return "%s" %(self.products.count())

	class Meta:
		verbose_name = "My Products"
		verbose_name_plural = "My Products"





























