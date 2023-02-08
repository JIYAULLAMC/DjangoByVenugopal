import email
from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
