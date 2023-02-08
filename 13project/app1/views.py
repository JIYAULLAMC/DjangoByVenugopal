from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from app1.forms import ProductForm
from app1.models import ProductModel

# Create your views here.

def create_product(request):
    pform = ProductForm()
    if request.method=='POST':
        form_data = ProductForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpRequest('record is created ')
    return render(request, 'index.html',{'pform':pform})

def update_product(request, pk):
    pre_data = ProductModel.objects.get(pid=pk)
    pform = ProductForm(instance = pre_data)
    if request.method =='POST':
        print("-----------------",pre_data)     
        form_data = ProductForm(request.POST, instance=pre_data)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('data updated !')
    return render(request, 'index.html',{'pform': pform})
