from django.contrib import admin
from app1.models import ItemModel, ProductModel
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ['iid', 'iname', 'iprice']

admin.site.register(ItemModel, ItemAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid', 'pname', 'pprice','pdesc','iid']

admin.site.register(ProductModel, ProductAdmin)


