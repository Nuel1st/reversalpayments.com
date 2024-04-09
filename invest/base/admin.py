from django.contrib import admin
from . models import Customer, Product, UserProfile
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category' ]

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'zipcode', 'country' ]

admin.site.register(UserProfile)