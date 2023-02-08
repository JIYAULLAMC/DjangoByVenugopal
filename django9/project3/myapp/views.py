from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import registermodel
# Create your views here.
def registerview(request):
    if request.method=='POST':
        print(request.POST)
        registermodel.objects.create(username=request.POST['username'],
        email=request.POST['email'],
        phone=request.POST['phone'],
        age=request.POST['age'],
        password=request.POST['password'])
        return HttpResponse("data is stored")
    return render(request,'register.html')


def listview(request):
    res=registermodel.objects.all()
    return render(request,'list.html',{'res':res})

def detailview(request,pk):
    res=registermodel.objects.filter(id=pk)
    return render(request,'list.html',{'res':res})

def updateview(request,pk):
    res=registermodel.objects.get(id=pk)
    if request.method=='POST':
        print(request.POST)
        registermodel.objects.filter(id=pk).update(username=request.POST['username'],
        email=request.POST['email'],
        phone=request.POST['phone'],
        age=request.POST['age'],
        password=request.POST['password'])
        return HttpResponse("data is updated")
    return render(request,'update.html',{'res':res})

def deleteview(request,pk):
    res=registermodel.objects.get(id=pk)
    if request.method=='POST':
        registermodel.objects.filter(id=pk).delete()
        return HttpResponse("data is deleted")
    return render(request,'deleteconfirm.html',{'res':res})