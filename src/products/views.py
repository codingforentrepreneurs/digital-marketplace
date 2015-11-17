from django.http import Http404
from django.shortcuts import render, get_object_or_404
# Create your views here.

from .models import Product

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