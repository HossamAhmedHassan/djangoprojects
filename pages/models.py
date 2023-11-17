from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
    res_choices = [
        ('restaurant1','restaurant1'),
        ('restaurant2','restaurant2'),
        ('restaurant3','restaurant3'),
        ('restaurant4','restaurant4'),
        ('restaurant5','restaurant5'),
        ('restaurant6','restaurant6'),
    ]
    title       = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True,max_length=50)
    price       = models.DecimalField(max_digits=5,decimal_places=0)
    image       = models.ImageField(upload_to='photos/%y/%m/%d')
    restaurant  = models.CharField(max_length=50,choices=res_choices)
    active      = models.BooleanField()


class Movingdata(models.Model):
    id = models.IntegerField(primary_key=True, serialize=False,default=0)
    count = models.IntegerField()
    restaurant = models.CharField(max_length=50,editable=False,null=True)


class Movingtoorders(models.Model):
    restaurant = models.CharField(max_length=50)
    totalamount = models.IntegerField()
    time = models.TimeField(default=datetime.now,editable=False)
    date = models.DateField(default=datetime.now,editable=False)

class MovedData(models.Model):
    restaurant = models.CharField(max_length=50)
    totalamount = models.IntegerField()
    time = models.TimeField()
    date = models.DateField()
    class Meta:
        ordering=['-id']