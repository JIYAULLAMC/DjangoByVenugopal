from django.db import models
from django.contrib.auth.models import User
from authe.validators import *
# Create your models here.

class registermodel(User):
    phone=models.PositiveBigIntegerField()
    gender=models.CharField(max_length=10,choices=[['Male','Male'],['Female','Female']])
    
