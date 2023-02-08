from ast import mod
from distutils.command.upload import upload
from random import choices
from turtle import mode
from django.db import models

# Create your models here.

class Cloth(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    offer = models.IntegerField()
    genders = [["male","male"],["female", "female"]]    
    gender = models.CharField(max_length=50, choices=genders)
    color = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    cloth_sizes = [['small','small'], ['mediam','mediam'],['long','long']]
    size = models.CharField(max_length=50, choices=cloth_sizes)
    desc = models.TextField()
    photo = models.ImageField(upload_to="clothpics")
