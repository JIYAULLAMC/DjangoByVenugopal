from django.db import models

# Create your models here.

class bank(models.Model):
    bname=models.CharField(max_length=30)
    nofcust=models.IntegerField()
    phone=models.PositiveBigIntegerField()

class vbank(bank):
    ifsc=models.CharField(max_length=15)
    address=models.CharField(max_length=100)