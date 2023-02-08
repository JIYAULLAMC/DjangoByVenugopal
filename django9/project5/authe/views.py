from django.http import HttpResponse
from django.shortcuts import redirect, render
from authe.forms import registerform,loginform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def registerview(request):
    form=registerform()
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/login/')
    return render(request,'register.html',{'form':form})

def loginview(request):
    form=loginform()
    if request.method=='POST':
        form=loginform(request.POST)
        try:
            if form.is_valid:
                user=authenticate(username=request.POST['username'],password=request.POST['password'])
                if user is not None:
                    login(request,user)
                    messages.success(request,"your login is success")
                    return redirect('/home/')
                else:
                    messages.error(request,"your login id and password is incorrect")
            messages.error(request,"check login id and password")
        except:
            return redirect('/register/')
    return render(request,'register.html',{"form":form},status=201)

@login_required(login_url='/login/')
def logoutview(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def homeview(request):
    return render(request,'home.html')
