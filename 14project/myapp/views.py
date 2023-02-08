from django.http import HttpResponse
from django.shortcuts import render
from myapp.forms import RegisterForm

# Create your views here.


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            HttpResponse('record is created')

    return render(request, 'register.html',{'form': form})
