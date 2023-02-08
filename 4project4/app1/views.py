from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request):
    if request.method=="POST":
        return HttpResponse("the data is created")
    return render(request, 'login.html')
