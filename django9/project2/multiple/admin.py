from django.contrib import admin
from multiple.models import customer,product,register
# Register your models here.


class customeradmin(admin.ModelAdmin):
    list_display=['cid','cname','email','phone']

class productadmin(admin.ModelAdmin):
    list_display=['pid','pname','desc','price','discount','stock']

class registeradmin(admin.ModelAdmin):
    list_display=['cid','pid','cname','email','phone','pname','desc','price','discount','stock','address','shopaddress','lino']


admin.site.register(customer,customeradmin)
admin.site.register(product,productadmin)
admin.site.register(register,registeradmin)