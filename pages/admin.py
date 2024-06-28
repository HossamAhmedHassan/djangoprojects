from django.contrib import admin
from .models import Product,Restaurant,CartProduct,Order
# Register your models here.
class ProductMeta(admin.ModelAdmin):
    list_display = ['title','price']
class RestaurantMeta(admin.ModelAdmin):
     list_display = ['name']

class CartProductMeta(admin.ModelAdmin):
     list_display = ['product']

class OrderMeta(admin.ModelAdmin):
     list_display = ['restaurant']
     
admin.site.register(Product,ProductMeta)
admin.site.register(Restaurant,RestaurantMeta)
admin.site.register(CartProduct,CartProductMeta)
admin.site.register(Order,OrderMeta)