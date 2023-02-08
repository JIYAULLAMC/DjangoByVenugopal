from django import forms


class StudentForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number= forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(max_length=100)