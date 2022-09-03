from django.contrib import admin

from .models import Banner


class BannerAdmin(admin.ModelAdmin):
  list_display = ['name', 'image']
  search_fields = ['name', 'image']

admin.site.register(Banner, BannerAdmin)
