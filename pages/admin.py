from django.contrib import admin
from .models import Product,MovingData
# Register your models here.
class HossamAdmin(admin.ModelAdmin):
     list_display = ['title','price']
admin.site.register(Product,HossamAdmin)
admin.site.register(MovingData)

