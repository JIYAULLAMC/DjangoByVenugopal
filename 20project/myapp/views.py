from django.shortcuts import render, redirect
from myapp.forms import StudentForm,LoginForm
from django.http import HttpResponse
from myapp.models import Student
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def stu_create(request):
    form = StudentForm()
    if request.method == 'POST' and request.FILES:
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("your data is stored")
    return render(request, 'index.html', {'form': form})


def stu_list(request):
    students = Student.objects.all()
    return render(request, 'stu_list.html',{'students': students})


def stu_login(request):
    form = LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        try:
            if form.is_valid:
                print("------------------------------------------------------------------")
                user=authenticate(username=request.POST['firstname'],password=request.POST['lastname'])
                if user is not None:
                    login(request,user)
                    messages.success(request,"your login is success")
                    return redirect('/stu_list/')
                else:
                    messages.error(request,"your login id and password is incorrect")
            messages.error(request,"check login id and password")
        except:
            return redirect('/stu_create/')
    return render(request,'index.html',{"form":form},status=201)
        
