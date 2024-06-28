from . import views
from django.urls import path

urlpatterns =[
    path('',views.respage,name='respage'),
    # path('orders',views.orders,name='orders'),
    # path('cart',views.cart,name='cart'),
    # path('restaurant1',views.restaurant1,name='restaurant1'),
    # path('restaurant2',views.restaurant2,name='restaurant2'),
    # path('restaurant3',views.restaurant3,name='restaurant3'),
    # path('restaurant4',views.restaurant4,name='restaurant4'),
    # path('restaurant5',views.restaurant5,name='restaurant5'),
    # path('restaurant6',views.restaurant6,name='restaurant6'),
]