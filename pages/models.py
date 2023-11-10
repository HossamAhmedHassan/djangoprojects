from django.db import models

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


class MovingData(models.Model):
    id = models.IntegerField(primary_key=True)
    count = models.IntegerField()