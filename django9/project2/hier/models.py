from platform import processor
from django.db import models

# Create your models here.
class details(models.Model):
    pname=models.CharField(max_length=30)
    desc=models.CharField(max_length=130)
    price=models.FloatField()
    discount=models.FloatField()
    stock=models.IntegerField()

class mobile(details):
    proc=models.CharField(max_length=20)
    ram=models.CharField(max_length=20)
    rom=models.CharField(max_length=20)
    camera=models.CharField(max_length=30)
    battery=models.CharField(max_length=30)

class laptop(details):
    proc=models.CharField(max_length=20)
    ram=models.CharField(max_length=20)
    rom=models.CharField(max_length=20)
    os=models.CharField(max_length=30)
    battery=models.CharField(max_length=30)

