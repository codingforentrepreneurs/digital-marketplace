from django.contrib import admin

# Register your models here.

from .models import Transaction

admin.site.register(Transaction)