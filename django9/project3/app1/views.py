from django.http import HttpResponse
from django.shortcuts import render
from app1.forms import registerform
from app1.models import registermodel
# Create your views here.
def homeview(request):
    form=registerform()
    print(form)
    if request.method=='POST':
        registermodel.objects.create(
            name=request.POST['name'],
            firstname=request.POST['firstname'],
            age=request.POST['age'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            gender=request.POST['gender'],
            date=request.POST['date'])
        return HttpResponse('data is stored')
    return render(request,'home.html',{'form':form})


def detailview(request):
    res=registermodel.objects.all()
    return HttpResponse(res)


def updateview(request,pk):
    res=registermodel.objects.get(id=pk)
    if request.method=='POST':
        registermodel.objects.filter(id=pk).update(
            name=request.POST['name'],
            firstname=request.POST['firstname'],
            age=request.POST['age'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            gender=request.POST['gender'],
            date=request.POST['date'])
        return HttpResponse('data is updated')
    return render(request,'rupdate.html',{'res':res})


def deleteview(request,pk):
    registermodel.objects.filter(id=pk).delete()
    return HttpResponse('data is deleted')
    

