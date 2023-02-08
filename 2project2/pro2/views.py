from django.http import HttpResponse


def data_from_front(request,data):
    return HttpResponse(data)

def addition(request,var1, var2):
    res = int(var1)+int(var2)
    return HttpResponse(res)