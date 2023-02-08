from django.shortcuts import render
from myapp.forms import StudentForm
from django.http import HttpResponse
# Create your views here.

def create_stu(request):
    form = StudentForm()
    if request.method=="POST" and request.FILES:
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("data is stored")
    return render(request, 'index.html',{'form':form})
