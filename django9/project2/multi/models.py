from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.PositiveBigIntegerField()

class address(person):
    dno=models.CharField(max_length=30)
    street=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=30)

class bank(address):
    bname=models.CharField(max_length=30)
    hname=models.CharField(max_length=50)    

