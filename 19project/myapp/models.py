import email
from operator import mod
from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='studentpics/')
    
