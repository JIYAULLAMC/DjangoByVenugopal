from django.contrib import admin
from app1.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'password']

admin.site.register(Student, StudentAdmin)