from turtle import mode
from xml.parsers.expat import model
from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=100)
    ptype = [["fashion", "fashion"],["menfashion","menfashion"],['menfashion','menfashion'],['kids','kids'],
    ["books","books"],['mobile','mobile'],["computer","computer"],["laptop","laptop"],["sprots","sprots"],["kitchen_items","kitchen_items"],
    ["health","health"],["groceries","groceries"],["movies/songs","movies/songs"]]
    producttype = models.CharField(max_length=50, choices=ptype)
    genders = [["male","male"],["female", "female"]]    
    gender = models.CharField(max_length=50, choices=genders)
    color = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    offer = models.IntegerField()
    price = models.IntegerField()
    product_sizes = [['small','small'], ['mediam','mediam'],['long','long']]
    size = models.CharField(max_length=50, choices=product_sizes)
    desc = models.TextField()
    photo = models.ImageField(upload_to="productpics")
