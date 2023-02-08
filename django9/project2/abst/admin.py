from django.contrib import admin
from abst.models import student,tstaff,ntstaff
# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','address','doj','course','fee']

admin.site.register(student,studentadmin)

class tstaffadmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','address','doj','quali','course','salary']

admin.site.register(tstaff,tstaffadmin)

class ntstaffadmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','address','doj','quali','salary']

admin.site.register(ntstaff,ntstaffadmin)