from django import forms
from cbv.models import samplemodel
class sampleform(forms.ModelForm):
    class Meta:
        model=samplemodel
        fields='__all__'