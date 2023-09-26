from django.shortcuts import render

# Create your views here.
def respage(request):

    return render(request,'respage/respage.html')

def orders(request):
    
    return render(request,'orders/orders.html')

def cart(request):
    
    return render(request,'cart/cart.html')

def restaurant1(request):
    
    return render(request,'restaurants/restaurant1.html')

def restaurant2(request):
    
    return render(request,'restaurants/restaurant2.html')

def restaurant3(request):
    
    return render(request,'restaurants/restaurant3.html')

def restaurant4(request):
    
    return render(request,'restaurants/restaurant4.html')

def restaurant5(request):
    
    return render(request,'restaurants/restaurant5.html')

def restaurant6(request):
    
    return render(request,'restaurants/restaurant6.html')