from django.db import models
from datetime import datetime
from .choices import *
# Create your models here.
# make average main price in the views
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    rate = models.CharField(max_length=50,choices=rate_choices)
    image = models.ImageField(upload_to='resturants_photos/%y/%m/%d')
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model): 
    title       = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True,max_length=200)
    price       = models.DecimalField(max_digits=5,decimal_places=0)
    image       = models.ImageField(upload_to='products_photos/%y/%m/%d')
    restaurant  = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
    active      = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    
