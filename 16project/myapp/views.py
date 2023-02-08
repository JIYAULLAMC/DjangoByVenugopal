from django.shortcuts import render
from myapp.forms import StudentForm

# Create your views here.

def home(request):
    form = StudentForm()
    return render(request, 'home.html', {"form" : form})
