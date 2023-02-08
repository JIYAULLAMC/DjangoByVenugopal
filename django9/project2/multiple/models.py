from django.db import models

# Create your models here.
class customer(models.Model):
    cid=models.BigAutoField(primary_key=True)
    cname=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.PositiveBigIntegerField()

class product(models.Model):
    pid=models.BigAutoField(primary_key=True)
    pname=models.CharField(max_length=30)
    desc=models.CharField(max_length=130)
    price=models.FloatField()
    discount=models.FloatField()
    stock=models.IntegerField()

class register(customer,product):
    address=models.CharField(max_length=20)
    shopaddress=models.CharField(max_length=20)
    lino=models.CharField(max_length=20)