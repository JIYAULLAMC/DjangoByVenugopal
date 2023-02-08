from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def app_home(request):
    return HttpResponse("Hello this is app home")


def app_index(request):
    return render(request, "app_index.html")

def app_view(request):
    return HttpResponse("this is app_view functions ")

class person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

obj = person("gokul",20)

def home(request):
    data = "this is my work"
    data = ("a",10,"b",20)
    return render(request,"home.html", {"data":obj})
