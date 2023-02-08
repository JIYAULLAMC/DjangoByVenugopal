from django.contrib import admin
from myapp.models import registermodel
# Register your models here.
class registeradmin(admin.ModelAdmin):
    list_display=['id','username','email','phone','age','password']

admin.site.register(registermodel,registeradmin)
