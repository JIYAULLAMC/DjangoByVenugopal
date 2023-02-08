from operator import ipow
from pyexpat import model
from django import forms
from app1.models import Student

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(max_length=50)



