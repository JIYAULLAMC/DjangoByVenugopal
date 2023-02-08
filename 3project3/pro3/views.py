from django.shortcuts import render

# def home(request):
#     return render(request, "home.html")
    
# def base(request):
#     return render(request, "base.html")


# # help to send or request the data from one file to another file\

# def datahome(request,ind, data):
#     return render(request, "datahome.html",{"ind": ind,'data':data})
    
# def database(request):
#     data = "this is my home i will not leve"
#     ind=1
#     return render(request, "database.html",{"data":data,"ind":ind})



def shome(request,data):
    return render(request, 'shome.html',{'data':data}) 


def sbase(request):
    data = "jiya "
    return render(request, 'sbase.html',{"data": data}) 