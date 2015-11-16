from django.shortcuts import render

# Create your views here.


def detail_view(request):
	# 1 item
	print request
	template = "detail_view.html"
	context = {}
	return render(request, template, context)



def list_view(request):
	# list of items
	print request
	template = "list_view.html"
	context = {}
	return render(request, template, context)