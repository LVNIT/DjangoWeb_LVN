from django.contrib import admin

from .models import *


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display = ['brand_id', 'created_by','title','slug', 'image', 'description', 'price']
    prepopulated_fields = {'slug': ('title',)}

