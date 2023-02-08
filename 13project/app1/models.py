from tkinter import CASCADE
from django.db import models

# Create your models here.

class ItemModel(models.Model):
    iid = models.BigAutoField(primary_key=True)
    iname = models.CharField(max_length=50)
    iprice = models.IntegerField()

    def __str__(self):
        return self.iname


class ProductModel(models.Model):
    pid = models.BigAutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    pprice = models.IntegerField()
    pdesc = models.TextField()
    iid = models.ForeignKey(ItemModel, on_delete=models.CASCADE)

