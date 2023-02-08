from django.contrib import admin
from clothapp.models import Cloth

# Register your models here.


class ClothAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'offer','gender', 'color', 'brand','size', 'desc','photo']


admin.site.register(Cloth, ClothAdmin)