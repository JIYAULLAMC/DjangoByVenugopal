from django.contrib import admin
from myapp.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number','email','password' ]

admin.site.register(Student, StudentAdmin)


