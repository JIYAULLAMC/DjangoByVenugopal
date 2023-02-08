from django.contrib import admin
from multi.models import person,address,bank
# Register your models here.

class personadmin(admin.ModelAdmin):
    list_display=['name','email','phone']

class addressadmin(admin.ModelAdmin):
    list_display=['name','email','phone','dno','street','city','state','country']

class bankadmin(admin.ModelAdmin):
    list_display=['name','email','phone','dno','street','city','state','country','bname','hname']


admin.site.register(person,personadmin)
admin.site.register(address,addressadmin)
admin.site.register(bank,bankadmin)
