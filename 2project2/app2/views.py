from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'ap2home.html') 


def register(request):
    print(request)
    return render(request, "register.html")
