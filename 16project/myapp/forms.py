from tkinter import Widget
from django import forms
from myapp.models import Student


class StudentForm(forms.ModelForm):  
    class Meta : 
        model = Student
        fields = ['id', 'roll', 'name', 'address']

        widgets = {
        "name" : forms.TextInput(attrs={'class' : "form-control", "placeholder": "name"}),
        "roll" : forms.TextInput(attrs={'class' : "form-control", "placeholder": "roll"}),
        "address" : forms.TextInput(attrs={'class' : "form-control", "placeholder": "address"}),
        }

