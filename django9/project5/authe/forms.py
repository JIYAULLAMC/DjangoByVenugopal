from django import forms
from authe.models import registermodel
from django.contrib.auth.hashers import make_password


class registerform(forms.ModelForm):
    repassword= forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=registermodel
        fields=['username','first_name','last_name','email','phone','gender','password']
    
    def save(self, commit=True):
        user1=super().save(commit=False)
        user1.password=make_password(user1.password)
        if commit and user1:
            print(user1.phone)
            user1.save()

class loginform(forms.ModelForm):
    class Meta:
        model=registermodel
        fields=['username','password']