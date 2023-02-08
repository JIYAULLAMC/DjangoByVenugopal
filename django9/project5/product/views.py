from django.http import HttpResponse
from django.shortcuts import render
from django.urls import is_valid_path
from product.forms import productform
from product.models import productmodel
# Create your views here.

def productview(request):
    form=productform()
    if request.method=="POST" and request.FILES:
        form=productform(request.POST,request.FILES)
        if form.is_valid():
            print("haii")
            form.save()
            return HttpResponse("data is stored")
    return render(request,'product.html',{'form':form})


def productupdate(request,pk):
    res=productmodel.objects.get(pid=pk)
    form=productform(instance=res)
    if request.method=="POST" and request.FILES:
        form=productform(request.POST,request.FILES,instance=res)
        if form.is_valid():
            print("haii")
            form.save()
            return HttpResponse("data is updated")
    return render(request,'product.html',{'form':form})
