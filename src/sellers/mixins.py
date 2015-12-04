import datetime

from django.db.models import Count, Min, Sum, Avg, Max

from billing.models import Transaction
from digitalmarket.mixins import LoginRequiredMixin
from products.models import Product

from .models import SellerAccount



class SellerAccountMixin(LoginRequiredMixin, object):
	account = None
	products = []
	transactions = []

	def get_account(self):
		user = self.request.user
		accounts = SellerAccount.objects.filter(user=user)
		if accounts.exists() and accounts.count() == 1:
			self.account = accounts.first()
			return accounts.first()
		return None

	def get_products(self):
		account = self.get_account()
		products = Product.objects.filter(seller=account)
		self.products = products
		return products

	def get_transactions(self):
		products = self.get_products()
		transactions = Transaction.objects.filter(product__in=products)
		return transactions

	def get_transactions_today(self):
		today = datetime.date.today()
		today_min = datetime.datetime.combine(today, datetime.time.min)
		today_max = datetime.datetime.combine(today, datetime.time.max)
		return self.get_transactions().filter(timestamp__range=(today_min, today_max))

	def get_total_sales(self):
		transactions = self.get_transactions().aggregate(Sum("price"), Avg("price"))
		print transactions
		total_sales = transactions["price__sum"]
		return total_sales

	def get_today_sales(self):
		transactions = self.get_transactions_today().aggregate(Sum("price"))
		total_sales = transactions["price__sum"]
		return total_sales




