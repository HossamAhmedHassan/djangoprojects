from django.shortcuts import render
from .models import CartProduct,Order,Restaurant,Product
# Create your views here.

def respage(request):
    total_price_object = {}
    restaurant_products_count = {}
    average_price_object = {}

    for restaurant in Restaurant.objects.all():

        for product in Product.objects.all():

            if str(restaurant.name).lower() == str(product.restaurant).lower() :

                try:
                    average_price_object[restaurant.name] += product.price
                    restaurant_products_count[restaurant.name] += 1

                except:
                    average_price_object[restaurant.name] = product.price
                    restaurant_products_count[restaurant.name] = 1

        if f'{ restaurant.name }' in request.POST:
            productsList = []

            for product in Product.objects.all():

                if str(restaurant.name).lower() == str(product.restaurant).lower() :
                    productsList.append(product)

            respage_context = {'products':productsList}
            return render(request,'restaurant/restaurant.html',respage_context)

        average_price_object[restaurant.name] = f"{(average_price_object[restaurant.name] / restaurant_products_count[restaurant.name]):.2f}"
    
    respage_context = {'restaurantTable':Restaurant.objects.all(),"average_price_object":average_price_object}

    return render(request,'respage/respage.html',respage_context)

# ###########################################################################

# def orders(request):
#     if Movingtoorders.objects.count() != 0 :
#         for z in Movingtoorders.objects.all():
#             ordereddata = MovedData(restaurant=z.restaurant,totalamount=z.totalamount,time=z.time,date=z.date)
#             ordereddata.save()
#         Movingtoorders.objects.all().delete() 
#     Movingdata.objects.all().delete()

#     if request.method == 'POST':
#         if 'form_submission' in request.POST:
#             MovedData.objects.all().delete()

#     ordersContext = {'movetoorders':MovedData.objects.all()}
    
#     return render(request,'orders/orders.html',ordersContext)

# ###########################################################################


# def cart(request):
#     price=0
#     for x in Movingdata.objects.all():
#         if x.count == 0:
#             x.delete()
#         for res in Product.objects.all():
#             if res.id == x.id:
#                 price += (res.price * x.count)
    
#     Movingtoorders.objects.all().delete()

#     for x in Movingdata.objects.all():
#         restaurant = Product.objects.get(id = x.id).restaurant
#         totalamount = price + 20
#         if Movingtoorders.objects.count() == 0 and totalamount != None:
#             ordersdata = Movingtoorders(restaurant=restaurant,totalamount=totalamount)
#             ordersdata.save()

#         if f'trash{x.id}' in request.POST:
#             if x.count != 1:
#                 id = x.id
#                 restaurant = x.restaurant
#                 count = x.count - 1
#                 x.delete()
#                 data =Movingdata.objects.create(restaurant=restaurant,id=id,count=count)
#                 data.save()
                
#             elif x.count == 1:
#                 id = x.id
#                 x.delete()
#             price = price - int(Product.objects.get(pk = id).price)
                
#         if 'clearProducts' in request.POST:
#             x.delete()
#             price = 0
    
            
#         if 'Proceed' in request.POST and price != 0:
#             ordersContext = {'movetoorders':MovedData.objects.all()}
#             orders(request)
#             return render(request,'orders/orders.html',ordersContext)

#     cartContext = {'order_submit':False,'move':Movingdata.objects.all(),'pro':Product.objects.all(),'price':price ,'move_count':Movingdata.objects.count()}
#     return render(request,'cart/cart.html',cartContext)


# ############  RESTAURANTS FUNCTINS  ###############

# httpError = """<body style="display:flex ; align-items:center ; justify-content:space-around;" ><h1>  Cannot order from two restaurants in the same time please <h1/><a href="/" style="color:green;">Resturunts</a></body>"""

# def restaurantviewfunc(resNum,request):
#     context = {'pro':Product.objects.all(),'moveCount':Movingdata.objects.all().count()}
#     if Movingdata.objects.count() == 0 or Movingdata.objects.filter(restaurant=resNum).count() != 0:
#         for x in context.get('pro'):
#             if x.restaurant == resNum:  
#                 l = request.POST.get('id'+str(x.id))
#                 if l != None and l != 0:
#                     id = x.id
#                     count = l
#                     data = Movingdata(id=id,count=count,restaurant=resNum)
#                     data.save()

# ###########################################################################

# def restaurant1(request):
#     context = {'pro':Product.objects.all(),'moveCount':Movingdata.objects.all().count()}
#     restaurantviewfunc('restaurant1',request) 
#     if Movingdata.objects.count() == 0 or Movingdata.objects.filter(restaurant='restaurant1').count() != 0:print(end='')
#     else:
#         return HttpResponseNotFound(httpError)

#     return render(request,'restaurants/restaurant1.html',context)

# ###########################################################################

# def restaurant2(request):
#     context = {'pro':Product.objects.all(),'moveCount':Movingdata.objects.all().count()}
#     restaurantviewfunc('restaurant2',request)     
#     if Movingdata.objects.count() == 0 or Movingdata.objects.filter(restaurant='restaurant2').count() != 0:print()
#     else:
#         return HttpResponseNotFound(httpError)
#     return render(request,'restaurants/restaurant2.html',context)

# ###########################################################################

# def restaurant3(request):
#     context = {'pro':Product.objects.all(),'moveCount':Movingdata.objects.all().count()}
#     restaurantviewfunc('restaurant3',request)
#     if Movingdata.objects.count() == 0 or Movingdata.objects.filter(restaurant='restaurant3').count() != 0:print()
#     else:
#         return HttpResponseNotFound(httpError)
#     return render(request,'restaurants/restaurant3.html',context)

# ###########################################################################

# def restaurant4(request):
#     context = {'pro':Product.objects.all(),'moveCount':Movingdata.objects.all().count()}
#     restaurantviewfunc('restaurant4',request)    
#     if Movingdata.objects.count() == 0 or Movingdata.objects.filter(restaurant='restaurant4').count() != 0:print()
#     else:
#         return HttpResponseNotFound(httpError)
#     return render(request,'restaurants/restaurant4.html',context)

# ###########################################################################

# def restaurant5(request):
#     context = {'pro':Product.objects.all(),'moveCount':Movingdata.objects.all().count()}
#     restaurantviewfunc('restaurant5',request)  
#     if Movingdata.objects.count() == 0 or Movingdata.objects.filter(restaurant='restaurant5').count() != 0:print()
#     else:
#         return HttpResponseNotFound(httpError)
#     return render(request,'restaurants/restaurant5.html',context)

# ###########################################################################

# def restaurant6(request):
#     context = {'pro':Product.objects.all(),'moveCount':Movingdata.objects.all().count()}
#     restaurantviewfunc('restaurant6',request)   
#     if Movingdata.objects.count() == 0 and Movingdata.objects.filter(restaurant='restaurant6').count() != 0:print()
#     else:
#         return HttpResponseNotFound(httpError)
#     return render(request,'restaurants/restaurant6.html',context)
