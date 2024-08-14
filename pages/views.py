from django.shortcuts import render, redirect
from .models import Restaurant, Product
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
import math
from .forms import RestaurantCreate, ProductCreate
from django.urls import resolve,reverse
# Create your views here.

# hossam's part
Restaurants = Restaurant.objects.all()
Products = Product.objects.all()


@api_view(["GET"])
def main_page(request):
    Restaurants = Restaurant.objects.all()


    deleteId = request.GET.get("id")
    filteredRestaurants = Restaurants
    if deleteId != None:
        Restaurants.get(id=deleteId).delete()
        match = resolve(request.path)
        view_name = match.view_name
        view_args = match.kwargs
        query_params = request.GET.copy()
        query_params.pop("id", None)
        query_params.pop("currentPage", None)
        new_url = reverse(view_name, args=view_args, kwargs=query_params)
        return redirect(new_url)


    searchValue = request.GET.get("searchValue")
    if searchValue != None:
        filteredRestaurants = Restaurants.filter(name__contains=searchValue)
    paginationLength = math.ceil(filteredRestaurants.count() / 6)
    limitedRestaurant = Paginator(filteredRestaurants, 6)


    chosenPage = request.GET.get("chosenPage")
    currentPage = request.GET.get("currentPage")
    try:
        currentPage = int(currentPage) if currentPage else 1
    except (ValueError, TypeError):
        currentPage = 1


    average_product_price = {}
    for restaurant in Restaurants:
        try:
            total = (
                sum(
                    map(
                        lambda row: row[0],
                        Products.filter(restaurant=restaurant).values_list("price"),
                    )
                )
                / Products.filter(restaurant=restaurant).count()
            )
            average_product_price[restaurant] = total
        except:
            average_product_price[restaurant] = 0


    context = {
        "restaurants": limitedRestaurant.page(currentPage),
        "average_product_price": average_product_price,
        "currentPage": currentPage,
        "paginationLength": paginationLength,
        "filteredRestaurantsLength": filteredRestaurants.count(),
    }
    return render(request, "main_page/main_page.html", context)


def restaurant_menu(request):
    deleteId = request.GET.get("id")
    if deleteId != None:
        Products.get(id = deleteId).delete()
    restaurant_products = Products.filter(
        restaurant_id=Restaurants.get(id=(list(request.GET.dict())[0]))
    )

    context = {"restaurant_products": restaurant_products}
    return render(request, "restaurant/restaurant.html", context)


@api_view(["POST", "GET"])
def create_Restaurant(request):
    restaurant = None
    try:
       restaurant = Restaurants.get(id=request.GET.dict().get("id")) 
    except:
        pass
    action = "edit"
    if not restaurant:
        id = 0
        restaurant = Restaurant()
        action = "create"
    else:
        id = restaurant.id
    if request.method == "POST":
        restaurant_form = RestaurantCreate(
            request.POST, request.FILES, instance=restaurant
        )
        if restaurant_form.is_valid():
            restaurant = restaurant_form.save()
            return redirect("main_page")
    else:
        restaurant_form = RestaurantCreate(instance=restaurant)

    return render(
        request,
        "forms_templates/create_restaurant.html",
        {"form": restaurant_form, "action": action},
    )


@api_view(["POST", "GET"])
def create_Product(request):
    product = None
    try:
       product = Products.get(id=request.GET.dict().get("id")) 
    except:
        pass
    
    action = "edit"
    if not product:
        id = 0
        product = Product()
        action = "create"
    else:
        id = product.id
    if request.method == "POST":
        product_form = ProductCreate(
            request.POST, request.FILES, instance=product
        )
        if product_form.is_valid():
            product = product_form.save()
            return redirect("main_page")
    else:
        product_form = ProductCreate(instance=product)

    return render(request,"forms_templates/create_product.html",{"form": product_form, "action": action})


# bassem's part


# karem's part
