from django.shortcuts import render
from .models import Product,Movingdata,Movingtoorders,MovedData
from django.http import HttpResponseNotFound

# Create your views here.
def respage(request):
    return render(request,'respage/respage.html')

def orders(request):

    if Movingtoorders.objects.count() != 0 :
        for z in Movingtoorders.objects.all():
            ordereddata = MovedData(restaurant=z.restaurant,totalamount=z.totalamount,time=z.time,date=z.date)
            ordereddata.save()
        Movingtoorders.objects.all().delete() 

    ordersContext = {'movetoorders':MovedData.objects.all()}
    Movingdata.objects.all().delete()
    return render(request,'orders/orders.html',ordersContext)


price=0
objs = Movingdata.objects.all()
for x in objs:
    if x.count == 0:
        x.delete()
    for res in Product.objects.all():
        if res.id == x.id:
                price += (res.price * x.count)
CartContext = {'move':Movingdata.objects.all(),'pro':Product.objects.all(),'price':price}

def cart(request):
    Movingtoorders.objects.all().delete()
    objs2 = Movingdata.objects.all()
    for x in objs2:
        if x.id != None and x.count == 0:
            x.delete()
        restaurant = Product.objects.get(id = x.id).restaurant
        totalamount = price + 20
        if Movingtoorders.objects.count() == 0 and totalamount != None:
            ordersdata = Movingtoorders(restaurant=restaurant,totalamount=totalamount)
            ordersdata.save()

    return render(request,'cart/cart.html',CartContext)


context = {'pro':Product.objects.all()}


httpError = """
        <body style="display:flex ; align-items:center ; justify-content:space-around;" >
        <h1>  Cannot order from two restaurants in the same time please <h1/>
        <a href="/" style="color:green;">Resturunts</a>
        </body>
        """

def restaurantviewfunc(resNum,request):
    if Movingdata.objects.count() == 0 or Movingdata.objects.filter(restaurant=resNum).count() != 0:
        for x in context.get('pro'):
            if x.restaurant == resNum:  
                l = request.POST.get('id'+str(x.id))
                if l != None and l != 0:
                    id = x.id
                    count = l
                    data = Movingdata(id=id,count=count,restaurant=resNum)
                    data.save()

def restaurant1(request):
    restaurantviewfunc('restaurant1',request) 
    if Movingdata.objects.count() == 0 or Movingdata.objects.filter(restaurant='restaurant1').count() != 0:print(end='')
    else:
        return HttpResponseNotFound(httpError)

    return render(request,'restaurants/restaurant1.html',context)

def restaurant2(request):
    restaurantviewfunc('restaurant2',request)     
    if Movingdata.objects.count() == 0 or Movingdata.objects.filter(restaurant='restaurant2').count() != 0:print()
    else:
        return HttpResponseNotFound(httpError)
    return render(request,'restaurants/restaurant2.html',context)

def restaurant3(request):
    restaurantviewfunc('restaurant3',request)
    if Movingdata.objects.count() == 0 or Movingdata.objects.filter(restaurant='restaurant3').count() != 0:print()
    else:
        return HttpResponseNotFound(httpError)
    return render(request,'restaurants/restaurant3.html',context)

def restaurant4(request):
    restaurantviewfunc('restaurant4',request)    
    if Movingdata.objects.count() == 0 or Movingdata.objects.filter(restaurant='restaurant4').count() != 0:print()
    else:
        return HttpResponseNotFound(httpError)
    return render(request,'restaurants/restaurant4.html',context)

def restaurant5(request):
    restaurantviewfunc('restaurant5',request)  
    if Movingdata.objects.count() == 0 or Movingdata.objects.filter(restaurant='restaurant5').count() != 0:print()
    else:
        return HttpResponseNotFound(httpError)
    return render(request,'restaurants/restaurant5.html',context)

def restaurant6(request):
    restaurantviewfunc('restaurant6',request)   
    if Movingdata.objects.count() == 0 and Movingdata.objects.filter(restaurant='restaurant6').count() != 0:print()
    else:
        return HttpResponseNotFound(httpError)
    return render(request,'restaurants/restaurant6.html',context)

