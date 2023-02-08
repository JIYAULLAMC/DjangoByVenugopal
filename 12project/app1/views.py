import email
from django.http import HttpResponse
from django.shortcuts import render
from app1.forms import StudentForm
from app1.models import Student

# Create your views here.

def create_student(request):    
    sform = StudentForm()
    print(sform)
    if request.method == 'POST':        
        Student.objects.create(first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        phone= request.POST['phone'],
        email = request.POST['email'],
        password = request.POST['password'])
    return render(request, 'create_student.html', {'sform':sform})

def update_student(request,pk):
    sdata = Student.objects.get(id=pk)
    if request.method == 'POST':
        Student.objects.filter(id=pk).update(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        phone= request.POST['phone'],
        email = request.POST['email'],
        password = request.POST['password'])
        return HttpResponse("data is updated") 
    return render(request, 'update_student.html',{'sdata':sdata})


def read_student(request):
    res = Student.objects.all()
    data = ""
    for i in res:
        data = data + f'first name {i.first_name} last name {i.last_name} phone {i.phone} email {i.email} password {i.password}  '
        
    return HttpResponse(data)