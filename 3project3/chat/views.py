from django.shortcuts import render

# Create your views here.


def chome(request):
    return render(request, "chome.html")
    
def ccontact(request):
    return render(request, "ccontact.html")
