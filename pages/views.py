from django.shortcuts import render
from .models import Restaurant,Product
# Create your views here.

# hossam's part
# TODO: determine the method of the request to "GET" or use APIView
def main_page(requset):
    # TODO: implement the search functionality using django_filters
    # TODO: save the get_all_restaurants in a variable to avoid multiple calls at the for loop
    for restaurant in Restaurant.objects.all():
        # TODO: use the QuerySet ORM to get the average price instead of these for loops
        total_products_price = 0
        products_count = 0
        
        for product in Product.objects.all():
            if product.restaurant.name == restaurant.name:
                total_products_price += product.price
                products_count += 1
        if total_products_price > 0 and products_count > 0:
            # TODO: don't use unclear variable names like x again
            x = Restaurant.objects.get(name=restaurant.name) 
            x.average_product_price = total_products_price /products_count
            x.save()

    # TODO: use all restaurants variable instead of calling the query multiple times
    # TODO: pass the average_product_price to the context
    context = {'restaurant' : Restaurant.objects.all()}

    return render(requset,'main_page/main_page.html', context )



# TODO: determine the method of the request to "GET" or use APIView
def restaurant_menu(request):
    restaurant_products = []
    # TODO: get the restaurant name from the request.GET and use it in the filter
    for current_restaurant in request.GET:
        # TODO: use Product.objects.filter(restaurant__name__in=restaurant_name) instead of for loops
        # TODO: don't use get_all in the for loop
        for product in Product.objects.all():
            if product.restaurant.name == current_restaurant:
                restaurant_products.append(product)

    context = {'restaurant_products':restaurant_products}
    return render(request,"restaurant/restaurant.html",context)

# TODO: the templates is not styled at my side, please check it

# TODO: implement functions and templates to create new restaurants and products at the HTML page

# bassem's part



# karem's part