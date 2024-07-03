from django.shortcuts import render
from .models import Restaurant,Product
# Create your views here.

# hossam's part

def main_page(requset):
    
    for restaurant in Restaurant.objects.all():
        total_products_price = 0
        products_count = 0
        
        for product in Product.objects.all():
            if product.restaurant.name == restaurant.name:
                total_products_price += product.price
                products_count += 1
        if total_products_price > 0 and products_count > 0:
              
            x = Restaurant.objects.get(name=restaurant.name) 
            x.average_product_price = total_products_price /products_count
            x.save()
            
    context = {'restaurant' : Restaurant.objects.all()}

    return render(requset,'main_page/main_page.html', context )




def restaurant_menu(request):
    restaurant_products = []
    for current_restaurant in request.GET:
        for product in Product.objects.all():
            if product.restaurant.name == current_restaurant:
                restaurant_products.append(product)

    context = {'restaurant_products':restaurant_products}
    return render(request,"restaurant/restaurant.html",context)


# bassem's part



# karem's part