from django.db import models

# Create your models here.
class base(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.PositiveBigIntegerField()
    address=models.TextField()
    doj=models.DateField(auto_now_add=True)
    class Meta:
        abstract=True

class student(base):
    course=models.CharField(max_length=30)
    fee=models.IntegerField()

class tstaff(base):
    quali=models.CharField(max_length=30)
    salary=models.IntegerField()
    course=models.CharField(max_length=30)

class ntstaff(base):
    quali=models.CharField(max_length=30)
    salary=models.IntegerField()

