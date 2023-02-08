from django import forms
import re
def firstupper(value):
    if not(value[0].isupper()):
        raise forms.ValidationError("first letter should be uppercase")

def IsAlpha(value):
    if not(value.isalpha()):
            raise forms.ValidationError("first name should be alphabets")

def min_max(value): 
    if not(3<=len(value)<=20):
            raise forms.ValidationError("this field should be min 3 characters max 20 characters (you enter character len is %s)"%(len(value),))

def startsphone(value):
    if not(str(value)[0] in '6789'):
            raise forms.ValidationError("plz enter correct phone number")

def max10(value):
    if not(len(str(value))==10):
            raise forms.ValidationError("phone number should be ten digit")

def isnumeric(value):
    if re.findall('[0-9]+',value) == []:
            raise forms.ValidationError("this field should contain min one numeric value")
def isspecial(value):
    if re.findall('[^A-Za-z0-9]+',value)  == []:
            raise forms.ValidationError("password should contain min one special character")
