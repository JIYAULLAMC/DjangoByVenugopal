from django.db import models

# Create your models here.
class registermodel(models.Model):
    name=models.CharField(max_length=30)
    firstname=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.PositiveBigIntegerField()
    c=[['male','male'],['Female','Female']]
    gender=models.CharField(choices=c,max_length=10)
    date=models.DateField()
