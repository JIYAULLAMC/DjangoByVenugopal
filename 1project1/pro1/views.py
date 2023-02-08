from django.http import HttpResponse
from django.shortcuts import render


def cook(request):
    data = "this is dosa take and have it"
    return HttpResponse(data)


def home(request):
    mydata = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>home page</title>
        </head>
        <body>
            <h2> Hello World</h1>
            <marquee>this is second program </marquee>
        </body>
    </html>
    """
    return HttpResponse(mydata)

def index(request):
    # fobj = open(r"C:\Users\JiyaUlla\Desktop\Django\project1\index.html",'r')
    # data = fobj.read()
    # return HttpResponse(data)
    return render(request, "index.html")
    
def sample(request):
    return render(request, "sample.html")