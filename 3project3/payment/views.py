from django.shortcuts import render

# Create your views here.


def phome(request):
    return render(request, "phome.html")
    
def pcontact(request):
    return render(request, "pcontact.html")
