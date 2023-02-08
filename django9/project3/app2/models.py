from django.db import models

# Create your models here.

class itemmodel(models.Model):
    tid =models.BigAutoField(primary_key=True)
    tname=models.CharField(max_length=50)
    def __str__(self):
        return self.tname

class productmodel(models.Model):
    pid =models.BigAutoField(primary_key=True)
    pname=models.CharField(max_length=50)
    desc=models.TextField()
    price=models.PositiveIntegerField()
    discount=models.PositiveIntegerField()
    tid=models.ForeignKey(itemmodel,on_delete=models.CASCADE)
