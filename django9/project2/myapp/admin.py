from django.contrib import admin
from myapp.models import cricketmodel
# Register your models here.

class cricketadmin(admin.ModelAdmin):
    list_display=['id','name','gender','dob','matches','wins','loss','avg']

admin.site.register(cricketmodel,cricketadmin)

