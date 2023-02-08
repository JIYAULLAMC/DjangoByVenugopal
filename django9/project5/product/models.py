from distutils.command.upload import upload
from django.db import models

# Create your models here.

class productmodel(models.Model):
    pid=models.BigAutoField(primary_key=True)
    pname=models.CharField(max_length=50)
    pmodel=models.CharField(max_length=50)
    brand=models.CharField(max_length=50)
    desc=models.TextField()
    price=models.FloatField()
    discount=models.PositiveSmallIntegerField()
    pic=models.ImageField(upload_to='productpics/')

