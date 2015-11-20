from django.contrib import admin

# Register your models here.
from .models import Product, MyProducts, Thumbnail

class ThumbnailInline(admin.TabularInline):
	extra = 1
	model = Thumbnail


class ProductAdmin(admin.ModelAdmin):
	inlines = [ThumbnailInline]
	list_display = ["__unicode__", "description", "price", "sale_price"]
	search_fields = ["title", "description"]
	list_filter = ["price", "sale_price"]
	list_editable = ["sale_price"]
	class Meta:
		model = Product



admin.site.register(Product, ProductAdmin)


admin.site.register(MyProducts)