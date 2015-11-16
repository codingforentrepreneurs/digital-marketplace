from django.shortcuts import render

# Create your views here.

from .models import Product

def detail_view(request):
	# 1 item
	if request.user.is_authenticated():
		product = Product.objects.all().first()
		template = "detail_view.html"
		context = {
			"object": product
		}
	else:
		template = "not_found.html"
		context = {}
	return render(request, template, context)



def list_view(request):
	# list of items
	print request
	queryset = Product.objects.all()
	template = "list_view.html"
	context = {
		"queryset": queryset
	}
	return render(request, template, context)