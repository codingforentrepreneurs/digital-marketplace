from django.http import Http404
from django.shortcuts import render, get_object_or_404
# Create your views here.

from .forms import ProductAddForm, ProductModelForm
from .models import Product


def create_view(request): 
	form = ProductModelForm(request.POST or None)
	if form.is_valid():
		print form.cleaned_data.get("publish")
		instance = form.save(commit=False)
		instance.sale_price = instance.price
		instance.save()
	template = "create_view.html"
	context = {
			"form": form,
		}
	return render(request, template, context)


def update_view(request, object_id=None):
	product = get_object_or_404(Product, id=object_id)
	form = ProductModelForm(request.POST or None, instance=product)
	if form.is_valid():
		instance = form.save(commit=False)
		#instance.sale_price = instance.price
		instance.save()
	template = "update_view.html"
	context = {
		"object": product,
		"form": form,
		}
	return render(request, template, context)




def detail_slug_view(request, slug=None):
	product = Product.objects.get(slug=slug)
	try:
		product = get_object_or_404(Product, slug=slug)
	except Product.MultipleObjectsReturned:
		product = Product.objects.filter(slug=slug).order_by("-title").first()
	# print slug
	# product = 1
	template = "detail_view.html"
	context = {
		"object": product
		}
	return render(request, template, context)


def detail_view(request, object_id=None):
	product = get_object_or_404(Product, id=object_id)
	template = "detail_view.html"
	context = {
		"object": product
		}
	return render(request, template, context)

	# if object_id is not None:
	# 	product = get_object_or_404(Product, id=object_id)
	# 	# product = Product.objects.get(id=object_id)
	# 	# try:
	# 	# 	product = Product.objects.get(id=object_id)
	# 	# except Product.DoesNotExist:
	# 	# 	product = None

		
	# else:
	# 	raise Http404


def list_view(request):
	# list of items
	print request
	queryset = Product.objects.all()
	template = "list_view.html"
	context = {
		"queryset": queryset
	}
	return render(request, template, context)