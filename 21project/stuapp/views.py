from django.shortcuts import render
from stuapp.forms import StudentForm, StudentLogin
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, 'index.html')


def screate(request):
    form = StudentForm()
    if request.method == 'POST':
        print("-----------------------------------------------------")
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("the data is stored")
    return render(request, 'index.html', {'form': form})


def slogin(request):
    form = StudentLogin()
    if request.method == 'POST':
        form = StudentLogin(request.POST)
        if form.is_valid:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return HttpResponse("you have loged in ")
            else:
                return HttpResponse("your login id and password is incorrect")

    return render(request, 'index.html', {'form': form})


def slogout(request):
    form = StudentForm()
    return render(request, 'index.html', {'form': form})


# def screate(request):
#     form = StudentForm()
#     return render(request, 'index.html',{'form' : form})
