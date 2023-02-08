from django import forms
def firstupper(value):
    if not(value[0].isupper()):
        raise forms.ValidationError("this field first letter should be upper case")
    return value
    
def phone10(value):
    if len(str(value))!=10:
        raise forms.ValidationError("this field value should be 10 digits")
    return value