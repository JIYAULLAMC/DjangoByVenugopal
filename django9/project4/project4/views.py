from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request,'home.html')

@login_required(login_url='/accounts/login/')
def logoutview(request):
    logout(request)
    return redirect('/accounts/login/')