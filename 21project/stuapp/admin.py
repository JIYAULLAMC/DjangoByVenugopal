from django.contrib import admin
from stuapp.models import Student
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'phone', 'email', 'password']



admin.site.register(Student, StudentAdmin)