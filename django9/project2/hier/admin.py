from django.contrib import admin
from hier.models import details,mobile,laptop
# Register your models here.


class detailsadmin(admin.ModelAdmin):
    list_display=['id','pname','desc','price','discount','stock',]

class mobileadmin(admin.ModelAdmin):
    list_display=['id','pname','desc','price','discount','stock','proc','ram','rom','battery','camera']

class laptopadmin(admin.ModelAdmin):
    list_display=['id','pname','desc','price','discount','stock','proc','ram','rom','battery','os']


admin.site.register(details,detailsadmin)
admin.site.register(mobile,mobileadmin)
admin.site.register(laptop,laptopadmin)