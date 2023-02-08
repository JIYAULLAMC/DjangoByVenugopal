import email
from operator import mod
from django.db import models

# Create your models here.

class student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.PositiveBigIntegerField()
    stream = models.CharField(max_length=30)
    date = models.DateField()



class sample(models.Model):
    num1 = models.SmallIntegerField()
    num2 = models.IntegerField()
    num3 = models.BigIntegerField()
    num4 = models.PositiveSmallIntegerField()
    num5 = models.PositiveIntegerField()
    num6 = models.PositiveBigIntegerField()
    num7 = models.FloatField()
    num8 = models.DecimalField(max_digits=7,decimal_places=2)
    num9 = models.BooleanField()
    # num10 = models.NullBooleanField()
    num11 = models.BinaryField()