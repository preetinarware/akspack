from django.shortcuts import render

# Create your views here.



def product(request):
    return render(request,'products.html')


def product_detail(request):
    return render(request,'product-detail.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

# def home(request):
#     return render(request,'index.html')