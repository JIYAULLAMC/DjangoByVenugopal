from dataclasses import field
from pyexpat import model
from django import forms
from clothapp.models import Cloth

class ClothForm(forms.ModelForm):
    class Meta:
        model = Cloth
        fields = "__all__"
