from formapp.validations import firstupper,IsAlpha,min_max,startsphone,max10,isnumeric,isspecial

from django import forms

class registerform(forms.Form):
    firstname=forms.CharField(validators=[firstupper,IsAlpha,min_max])
    email=forms.EmailField()
    phone=forms.IntegerField(validators=[startsphone,max10])
    age=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput,validators=[firstupper,min_max,isspecial,isnumeric])

'''
    def clean(self):
        name=self.cleaned_data['firstname']
        if not(name[0].isupper()):
            raise forms.ValidationError("first letter should be uppercase")
        if not(name.isalpha()):
            raise forms.ValidationError("first name should be alphabets")

        if not(3<=len(name)<=20):
            raise forms.ValidationError("first name should be min 3 characters max 20 characters (you enter character len is %s)"%(len(name),))

        phone=self.cleaned_data['phone']
        if not(str(phone)[0] in '6789'):
            raise forms.ValidationError("plz enter correct phone number")
        if not(len(str(phone))==10):
            raise forms.ValidationError("phone number should be ten digit")

        age=self.cleaned_data['age']
        if not(10<=age<=75):
            raise forms.ValidationError("age should be min 10 year and  max 75 years (you enter age is %s)"%(age,))

        p=self.cleaned_data['password']
        if not(5<=len(p)<=20):
            raise forms.ValidationError("password should be min 5 characters and  max 20 characters")
        if not(p[0].isupper()):
            raise forms.ValidationError("password first_letter should be uppercase")
        if re.findall('[0-9]+',p) == []:
            raise forms.ValidationError("password should contain min one numeric value")
        if re.findall('[^A-Za-z0-9]+',p)  == []:
            raise forms.ValidationError("password should contain min one special character")

'''    
        



'''
    def clean_phone(self):
        phone=self.cleaned_data['phone']
        if not(str(phone)[0] in '6789'):
            raise forms.ValidationError("plz enter correct phone number")
        if not(len(str(phone))==10):
            raise forms.ValidationError("phone number should be ten digit")
        return phone

    def clean_firstname(self):
        name=self.cleaned_data['firstname']
        if not(name[0].isupper()):
            raise forms.ValidationError("first letter should be uppercase")
        if not(name.isalpha()):
            raise forms.ValidationError("first name should be alphabets")

        if not(3<=len(name)<=20):
            raise forms.ValidationError("first name should be min 3 characters max 20 characters (you enter character len is %s)"%(len(name),))
        return name

    def clean_age(self):
        age=self.cleaned_data['age']
        if not(10<=age<=75):
            raise forms.ValidationError("age should be min 10 year and  max 75 years (you enter age is %s)"%(age,))
        return age

    def clean_password(self):
        p=self.cleaned_data['password']
        if not(5<=len(p)<=20):
            raise forms.ValidationError("password should be min 5 characters and  max 20 characters")
        if not(p[0].isupper()):
            raise forms.ValidationError("password first_letter should be uppercase")
        if re.findall('[0-9]+',p) == []:
            raise forms.ValidationError("password should contain min one numeric value")
        if re.findall('[^A-Za-z0-9]+',p)  == []:
            raise forms.ValidationError("password should contain min one special character")
        return p
'''