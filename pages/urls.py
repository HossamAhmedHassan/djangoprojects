from . import views
from django.urls import path

urlpatterns =[
    path('',views.main_page,name='main_page'),
    # TODO: use snake_case for urls
    path('Menu',views.restaurant_menu,name='restaurant_menu')
]