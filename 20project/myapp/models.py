from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    pic = models.ImageField(upload_to ='stupic')
