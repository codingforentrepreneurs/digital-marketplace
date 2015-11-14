from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "description", "price", "sale_price"]
	search_fields = ["title", "description"]
	list_filter = ["price", "sale_price"]
	list_editable = ["sale_price"]
	class Meta:
		model = Product


admin.site.register(Product, ProductAdmin)