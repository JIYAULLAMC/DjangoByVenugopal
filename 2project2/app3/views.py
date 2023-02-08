from django.shortcuts import render

# Create your views here.

class persone:
    def __init__(self, firstaname, middlename, lastname, age, salary):
        self.firstaname = firstaname
        self.middlename = middlename
        self.lastname = lastname
        self.age = age
        self.salary = salary
       
a= persone("AAAAA","Aa","aaaa",12,10000)
b= persone("BBBB","Bb","bbbb",20,20000)
c= persone("CCCC","Cc","cccc",30,30000)
d= persone("DDDDD","Dd","ddddd",40,40000)

li = [a,b,c,d]
def home3(request,status):    
    return render(request,"home3.html",{"status":status,"list":li})


def filters(request):    
    data = {"var" : "jiyAUllA is a Bad person On The PLANet","var1":[1,2,3,5,2,4,6,3,5,67,4]}
    return render(request,"filters.html",data)
