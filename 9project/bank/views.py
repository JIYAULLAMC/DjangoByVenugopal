from django.http import HttpResponse
from django.shortcuts import render
from bank.models import bankmodel

# Create your views here.


def createview(request, bid, bname, ifsc):
    bankmodel.objects.create(bid=bid,bname=bname,ifsc=ifsc)
    return HttpResponse('data created')

def updateview(request, bid, bname):
    bankmodel.objects.filter(bid=bid).update(bname=bname)
    return HttpResponse('data updated')

def deleteview(request, bid):
    bankmodel.objects.filter(bid=bid).delete()
    return HttpResponse('data created')

def listview(request):
    res = bankmodel.objects.all()
    print("--------------------",res)
    return render(request, 'list.html',{'res':res})


