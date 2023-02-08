import email
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class Student(User):
     phone = models.PositiveBigIntegerField()

