from django.shortcuts import render
from .models import Product

# Create your views here.
def respage(request):

    return render(request,'respage/respage.html')

def orders(request):
    
    return render(request,'orders/orders.html')

def cart(request):
    
    return render(request,'cart/cart.html')

context = {'pro':Product.objects.all()}

def restaurant1(request):
    
    return render(request,'restaurants/restaurant1.html',context)

def restaurant2(request):
    
    return render(request,'restaurants/restaurant2.html',context)

def restaurant3(request):
    
    return render(request,'restaurants/restaurant3.html',context)

def restaurant4(request):
    
    return render(request,'restaurants/restaurant4.html',context)

def restaurant5(request):
    
    return render(request,'restaurants/restaurant5.html',context)

def restaurant6(request):
    
    return render(request,'restaurants/restaurant6.html',context)