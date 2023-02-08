import email
from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)
