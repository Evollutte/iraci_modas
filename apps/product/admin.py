from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'category', 'size', 'amount', 'price', 'image']
  search_fields = ['name', 'category', 'size', 'amount', 'price', 'image']

admin.site.register(Product, ProductAdmin)
