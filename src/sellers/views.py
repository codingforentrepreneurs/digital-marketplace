from django.shortcuts import render
from django.views.generic import View
# Create your views here.

from digitalmarket.mixins import LoginRequiredMixin

from .forms import NewSellerForm

class SellerDashboard(LoginRequiredMixin, View):

	def post(self, request, *args, **kwargs):
		form = NewSellerForm(request.POST)
		if form.is_valid():
			print "make the user apply model"
		return render(request, "sellers/dashboard.html", {"form":form})


	def get(self, request, *args, **kwargs):
		form = NewSellerForm()
		return render(request, "sellers/dashboard.html", {"form":form})