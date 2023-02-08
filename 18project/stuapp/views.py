from django.http import HttpResponse
from django.shortcuts import render,redirect
#from stuapp.models import Student
from stuapp.forms import StudentForm, StudentLogin
from django.contrib.auth import authenticate,login,logout


# Create your views here.


def home(request):
    return render(request, 'home.html')


def slist(request):
    students = Student.objects.all()
    return render(request, 'slist.html',{'students' : students})

def screate(request):
    form = StudentForm()
    if request.method == 'POST':
        print('request is----------- ', request.POST)
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("the student data is received")
    return render(request, 'screate.html',{'form' : form})

def supdate(request, pk):
    id = pk
    data = Student.objects.get(id=pk)
    form = StudentForm(instance=data)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=data)
        if form.is_valid:
            form.save()
            return HttpResponse("the student data is received")
    return render(request, 'supdate.html',{'form' : form})


def sdelete(rquest,pk):
    id = pk
    Student.objects.get(id=pk).delete()
    return HttpResponse('data is removed')


def slogin(request):
    form = StudentLogin()
    if request.method == 'POST':
        form = StudentLogin(request.POST)
        print(request.POST['username'])
        print(request.POST['password'])
        if form.is_valid :
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            print(user)
            if user is not None:
                login(request, user)
                return HttpResponse("you have loged in")

            else : 
                return HttpResponse('check your credentials')
    return render(request, 'slogin.html',{'form':form})


def slogout(request):
    logout(request)
    return redirect('/slogin/')