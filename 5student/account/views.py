import email
import imp
from operator import mod
from django.shortcuts import render

from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method=='POST':
        print("----------------------------------------------------")
        print(request.POST['username'])
        print(request.POST['firstname'])
        print(request.POST['lastname'])
        print(request.POST['email'])
        print(request.POST['password1'])
        print(request.POST['password2'])

        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        # user = User.objects.create(username=username, firstname='firstname',lastname=lastname,email=email,password1=password1,password2=password2)
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>.',User.objects.all)
        # user.save()
        # print('user is created *******************************************************')
    else:
        print('++++++++++++++++++', request)



    return render(request, 'register.html')
