from django.db import models

# Create your models here.

class registermodel(models.Model):
    firstname=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.PositiveBigIntegerField()
    age=models.PositiveIntegerField()
    password=models.CharField(max_length=50)
