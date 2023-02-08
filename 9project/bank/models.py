from django.db import models

# Create your models here.


class bankmodel(models.Model):
    bid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=40)
    ifsc = models.CharField(max_length=20)


    def __str__(self):
        return self.bname

