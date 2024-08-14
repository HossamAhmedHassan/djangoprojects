from . import views
from django.urls import path

urlpatterns =[
    path('',views.main_page,name='main_page'),
    path('menu',views.restaurant_menu,name='restaurant_menu'),
    path('create_product',views.create_Product,name='create_product'),
    path('create_restaurant',views.create_Restaurant,name='create_restaurant'),
]