from django.db import models


# Create your models here.

class cricketmodel(models.Model):
    name=models.CharField(max_length=30)
    matches=models.IntegerField()
    wins=models.IntegerField()
    loss=models.IntegerField()
    avg=models.FloatField()
    gender=models.CharField(max_length=10,choices=[['MALE','Male'],['FEMALE','Female']])
    dob=models.DateField()
    def __str__(self):
        return self.name