from django.contrib import admin
from app2.models import itemmodel,productmodel


# Register your models here.

class itemadmin(admin.ModelAdmin):
    list_display=['tid','tname']

admin.site.register(itemmodel,itemadmin)

class productadmin(admin.ModelAdmin):
    list_display=['pid','pname','price','discount','desc','tid']

admin.site.register(productmodel,productadmin)