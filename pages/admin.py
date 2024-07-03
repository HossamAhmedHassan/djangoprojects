from django.contrib import admin
from .models import Product,Restaurant
# Register your models here.
class ProductMeta(admin.ModelAdmin):
    list_display = ['title','price']
class RestaurantMeta(admin.ModelAdmin):
     list_display = ['name']


     
admin.site.register(Product,ProductMeta)
admin.site.register(Restaurant,RestaurantMeta)
