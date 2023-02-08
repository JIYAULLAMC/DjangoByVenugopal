from http.client import HTTPResponse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView,FormView,CreateView
from cbv.forms import sampleform
from cbv.models import samplemodel
# Create your views here.

def func(request):
    form=sampleform()
    if request.method=='POST':
        form=sampleform(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("data is stored")
    return render(request,"func.html",{"form":form})

class ucbv(View):
    def get(self, request):
        form=sampleform()
        return render(request,"ucbv.html",{"form":form})
    
    def post(self,request):
        form=sampleform(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("data is stored")

class pcbv(FormView):
    template_name='pcbv.html'
    form_class=sampleform
    def form_valid(self, form):
        super().form_valid(form)
        form.save()
        return HttpResponse("data is stored")
    success_url='/func/'


class ccbv(CreateView):
    template_name="pcbv.html"
    model=samplemodel
    fields='__all__'
    context_object_name='form'
    success_url='/func/'





'''
def func(request):
    return HttpResponse("hello")

class ucbv(View):
    def get(self, request):
        return HttpResponse("hello django")

'''