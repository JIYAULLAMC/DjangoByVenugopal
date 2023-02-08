from django import forms
from myapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class LoginForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname']