from django.shortcuts import render
from django.views import View


# Create your views here.

def funcview(request):
    return render(request, 'tindex.html')


class EmpView(View):
    def get(self, request):
        return render(request, 'cindex.html')