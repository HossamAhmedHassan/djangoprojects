from . import views
from django.urls import path

urlpatterns =[
    path('',views.main_page,name='main_page'),
    path('menu',views.restaurant_menu,name='restaurant_menu')
]