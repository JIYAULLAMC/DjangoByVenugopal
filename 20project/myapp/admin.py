import imp
from django.contrib import admin
from myapp.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'pic']


admin.site.register(Student, StudentAdmin)