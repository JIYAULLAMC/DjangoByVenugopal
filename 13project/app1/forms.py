from pyexpat import model
from django import forms
from app1.models import ItemModel, ProductModel


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'
        
