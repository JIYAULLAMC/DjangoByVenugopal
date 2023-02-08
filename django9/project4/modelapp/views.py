from django.http import HttpResponse
from django.shortcuts import render

from modelapp.forms import registerform
from modelapp.models import registermodel
# Create your views here.
def registerview(request):
    form=registerform()
    print(form)
    if request.method=='POST':
        form=registerform(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data is stored")
    return  render(request,'index.html',{'form':form})


def updateview(request,pk):
    res=registermodel.objects.get(id=pk)
    form=registerform(instance=res)
    print(form)
    if request.method=='POST':
        form=registerform(request.POST,instance=res)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data is updated")
    return  render(request,'index.html',{'form':form})

def index(request):
    return render(request,'index.html')