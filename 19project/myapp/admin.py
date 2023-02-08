from django.contrib import admin
from myapp.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'phone', 'email', 'photo']

admin.site.register(Student, StudentAdmin)

