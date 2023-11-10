from django.shortcuts import render
from .models import Product,MovingData

# Create your views here.
def respage(request):

    return render(request,'respage/respage.html')

def orders(request):
    
    return render(request,'orders/orders.html')

price=0
objs = MovingData.objects.all()
for x in objs:
    if x.count == 0:
        x.delete()
    for res in Product.objects.all():
        if res.id == x.id:
                price += (res.price * x.count)
CartContext = {'move':MovingData.objects.all(),'pro':Product.objects.all(),'price':price}
def cart(request):
    for x in objs:
        if x.id != None:
            if x.count == 0:
                x.delete()
        

    return render(request,'cart/cart.html',CartContext)





context = {'pro':Product.objects.all()}

def restaurant1(request , *args , **kwargs):
        for x in context.get('pro'):
            if x.restaurant == 'restaurant1':  
                l = request.POST.get('id'+str(x.id))
                if l != None and l != 0:
                    id = x.id
                    count = l
                    data = MovingData(id=id,count=count)
                    data.save()
                    
        return render(request,'restaurants/restaurant1.html',context)

def restaurant2(request):
        for x in context.get('pro'):
            if x.restaurant == 'restaurant2':  
                l = request.POST.get('id'+str(x.id))
                if l != None and l != 0:
                    id = x.id
                    count = l
                    data = MovingData(id=id,count=count)
                    data.save()
        return render(request,'restaurants/restaurant2.html',context)

def restaurant3(request):
    for x in context.get('pro'):
        if x.restaurant == 'restaurant3':  
            l = request.POST.get('id'+str(x.id))
            if l != None and l != 0:
                id = x.id
                count = l
                data = MovingData(id=id,count=count)
                data.save()
    return render(request,'restaurants/restaurant3.html',context)

def restaurant4(request):
    for x in context.get('pro'):
        if x.restaurant == 'restaurant4':  
            l = request.POST.get('id'+str(x.id))
            if l != None and l != 0:
                id = x.id
                count = l
                data = MovingData(id=id,count=count)
                data.save()
    return render(request,'restaurants/restaurant4.html',context)

def restaurant5(request):
    for x in context.get('pro'):
        if x.restaurant == 'restaurant5':  
            l = request.POST.get('id'+str(x.id))
            if l != None and l != 0:
                id = x.id
                count = l
                data = MovingData(id=id,count=count)
                data.save()
    return render(request,'restaurants/restaurant5.html',context)

def restaurant6(request):
    for x in context.get('pro'):
        if x.restaurant == 'restaurant6':  
            l = request.POST.get('id'+str(x.id))
            if l != None and l != 0:
                id = x.id
                count = l
                data = MovingData(id=id,count=count)
                data.save()
    return render(request,'restaurants/restaurant6.html',context)

