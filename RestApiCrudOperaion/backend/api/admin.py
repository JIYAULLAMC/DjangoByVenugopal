from django.contrib import admin
from api.models import Students
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']


admin.site.register(Students, StudentAdmin)