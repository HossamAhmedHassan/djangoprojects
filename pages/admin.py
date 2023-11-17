from django.contrib import admin
from .models import Product,Movingdata,Movingtoorders,MovedData
# Register your models here.
class ProductMeta(admin.ModelAdmin):
     list_display = ['title','price']
class MovingdataMeta(admin.ModelAdmin):
     list_display = ['id']

class MovingtoordersMeta(admin.ModelAdmin):
     list_display = ['restaurant']

class MovedDataMeta(admin.ModelAdmin):
     list_display = ['date','restaurant']

admin.site.register(Product,ProductMeta)
admin.site.register(Movingdata,MovingdataMeta)
admin.site.register(Movingtoorders,MovingtoordersMeta)
admin.site.register(MovedData,MovedDataMeta)

