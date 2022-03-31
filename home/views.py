from django.shortcuts import render
from shop.models import *
# Create your views here.


def home(request):
    res={}
    res['product']=productDetail.objects.all()
    return render(request,'index.html',res)