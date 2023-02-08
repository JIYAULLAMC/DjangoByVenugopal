from django.contrib import admin
from productapp.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'producttype','gender','color','brand', 'offer','price','size','desc','photo']

admin.site.register(Product, ProductAdmin)