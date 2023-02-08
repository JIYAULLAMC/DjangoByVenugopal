from django.shortcuts import render
from myapp.forms import StudentForm

# Create your views here.


def createstudent(request):
    sform = StudentForm()
    return render(request,'create_student.html',{'sform':sform})

