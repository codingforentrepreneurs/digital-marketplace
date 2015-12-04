import datetime
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404


from billing.models import Transaction
from digitalmarket.mixins import LoginRequiredMixin
from products.models import Product

from .forms import NewSellerForm
from .mixins import SellerAccountMixin
from .models import SellerAccount





class SellerProductDetailRedirectView(RedirectView):
    permanent = True
    def get_redirect_url(self, *args, **kwargs):
        obj = get_object_or_404(Product, pk=kwargs['pk'])
        return obj.get_absolute_url()




class SellerTransactionListView(SellerAccountMixin, ListView):
	model = Transaction
	template_name = "sellers/transaction_list_view.html"

	def get_queryset(self):
		return self.get_transactions()




class SellerDashboard(SellerAccountMixin, FormMixin, View):
	form_class = NewSellerForm
	success_url = "/seller/"

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def get(self, request, *args, **kwargs):
		apply_form = self.get_form() #NewSellerForm()
		account = self.get_account()
		exists = account
		active = None
		context = {}
		if exists:
			active = account.active
		if not exists and not active:
			context["title"] = "Apply for Account"
			context["apply_form"] = apply_form
		elif exists and not active:
			context["title"] = "Account Pending"
		elif exists and active:
			context["title"] = "Seller Dashboard"
			today = datetime.date.today()
			today_min = datetime.datetime.combine(today, datetime.time.min)
			today_max = datetime.datetime.combine(today, datetime.time.max)
			print today, today_min, today_max
			#products = Product.objects.filter(seller=account)
			context["products"] = self.get_products()
			transactions_today = self.get_transactions().filter(timestamp__range=(today_min, today_max))
			context["transactions_today"] = transactions_today
			context["transactions"] = self.get_transactions().exclude(pk__in=transactions_today)[:5]
		else:
			pass
		
		return render(request, "sellers/dashboard.html", context)

	def form_valid(self, form):
		valid_data = super(SellerDashboard, self).form_valid(form)
		obj = SellerAccount.objects.create(user=self.request.user)
		return valid_data

