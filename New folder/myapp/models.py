import email
from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number= models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)