from django.http import HttpResponse
from django.shortcuts import render
from app2.forms import productform
from app2.models import productmodel
# Create your views here.
def productview(request):
    form=productform()
    if request.method=='POST':
        form=productform(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("data  is stored")
    return render(request,'rproduct.html',{'form':form})

def productupdate(request,pk):
    res=productmodel.objects.get(pid=pk)
    form=productform(instance=res)
    if request.method=='POST':
        form=productform(request.POST,instance=res)
        if form.is_valid:
            form.save()
            return HttpResponse("data  is update")
    return render(request,'rproduct.html',{'form':form})

def productread(request):
    res=productmodel.objects.all()
    return render(request,'readproduct.html',{'res':res})

def productdelete(request,pk):
    res=productmodel.objects.get(pid=pk).delete()
    return HttpResponse("data  is delete")