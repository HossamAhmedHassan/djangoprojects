from django.db import models
from datetime import datetime

# Create your models here.
# make averge main price in the views
class Restaurant(models.Model):
    # TODO: separate the choices to a separate file
    rate_choices = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]
    name = models.CharField(max_length=50)
    rate = models.CharField(max_length=50,choices=rate_choices,)
    # TODO: remove average_product_price from the model (it should be calculated in the views)
    average_product_price = models.IntegerField(editable=False,null=True,blank=True,default=0)
    image = models.ImageField(upload_to='resturants_photos/%y/%m/%d')
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model): 
    title       = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True,max_length=200)
    # TODO: set default value for price
    price       = models.DecimalField(max_digits=5,decimal_places=0)
    image       = models.ImageField(upload_to='products_photos/%y/%m/%d')
    restaurant  = models.ForeignKey(Restaurant,on_delete=models.PROTECT,null=True)
    # TODO: set default value for active
    active      = models.BooleanField()

    # TODO: set str method to the model