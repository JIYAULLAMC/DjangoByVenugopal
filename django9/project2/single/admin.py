from django.contrib import admin
from single.models import bank,vbank
# Register your models here.

class bankadmin(admin.ModelAdmin):
    list_display=['id','bname','phone','nofcust']

admin.site.register(bank,bankadmin)

class vbankadmin(admin.ModelAdmin):
    list_display=['id','bname','phone','nofcust','bank_ptr_id','ifsc','address']

admin.site.register(vbank,vbankadmin)