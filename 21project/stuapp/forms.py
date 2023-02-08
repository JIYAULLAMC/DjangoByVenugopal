from django import forms
from stuapp.models import Student
from django.contrib.auth.hashers import make_password


class StudentForm(forms.ModelForm):
    class Meta: 
        model = Student
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'password']

    def save(self, commit=True):
        user1=super().save(commit=False)
        user1.password=make_password(user1.password)
        if commit and user1:
            print(user1.phone)
            user1.save()




class StudentLogin(forms.ModelForm):
    class Meta: 
        model = Student
        fields = ['username', 'password']


