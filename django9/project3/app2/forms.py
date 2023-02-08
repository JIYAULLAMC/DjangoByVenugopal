from django import forms
from app2.models import productmodel


class productform(forms.ModelForm):
    class Meta:
        model=productmodel
        fields='__all__'
        #fields=['pname','desc']
        #exclude=['pname','desc']