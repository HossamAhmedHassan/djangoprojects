from django.shortcuts import render
from .models import Restaurant, Product
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
import math

# Create your views here.

# hossam's part
Restaurants = Restaurant.objects.all()
Products = Product.objects.all()

@api_view(['GET'])
def main_page(request):
    
    average_product_price = {}
    chosenPage = request.GET.get("chosenPage")
    currentPage = request.GET.get("currentPage")
    searchValue = request.GET.get("searchValue")
    filteredRestaurants = Restaurants
    if searchValue != None:
        filteredRestaurants = Restaurants.filter(name__contains=searchValue)
        
    paginationLength=math.ceil(filteredRestaurants.count() /6)
    limitedRestaurant = Paginator(filteredRestaurants,6)
    
    try:
        currentPage = int(currentPage) if currentPage else 1
    except (ValueError, TypeError):
        currentPage = 1
        
    for restaurant in Restaurants:
        try:
            total = sum(map(lambda row: row[0],Products.filter(restaurant=restaurant).values_list("price"))) / Products.filter(restaurant=restaurant).count()
            average_product_price[restaurant] = total
        except:
            average_product_price[restaurant] = 0
    context = {
        "restaurants": limitedRestaurant.page(currentPage),
        "average_product_price": average_product_price,
        'currentPage':currentPage,
        'paginationLength':paginationLength,
        'filteredRestaurantsLength':filteredRestaurants.count(),
    }
    return render(request, "main_page/main_page.html", context)


def restaurant_menu(request):
    restaurant_id = Restaurants.get(name=(list(request.GET.dict())[0])).id
    restaurant_products = Products.filter(restaurant_id=restaurant_id)

    context = {"restaurant_products": restaurant_products}
    return render(request, "restaurant/restaurant.html", context)


# bassem's part


# karem's part
