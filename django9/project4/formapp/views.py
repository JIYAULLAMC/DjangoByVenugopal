from django.http import HttpResponse
from django.shortcuts import render

from formapp.forms import registerform
from formapp.models import registermodel
# Create your views here.
def registerview(request):
    form=registerform()
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            #registermodel.objects.create(firstname=)
            return HttpResponse("data is stored")
    return  render(request,'register.html',{'form':form})