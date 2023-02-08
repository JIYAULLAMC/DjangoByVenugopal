from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField()
    phone = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)  

    def clean_name(self):
        name = self.cleaned_data['name']
        if not(name[0].isupper) :
            raise forms.ValidationError("enter valid input")
        if not(5<=len(name)<=20):
            raise forms.ValidationError('enter minimun 5 max 20')
        return name

    # def clean_password(self):
    #     pwd= self.cleaned_data['password']
    #     if not ()