import imp
from django.shortcuts import render
from .models import*
from django.core.paginator import Paginator
# Create your views here.


def blog(request):
    res={}
    blg=blog_detail.objects.all()
    
    paginator=Paginator(blg,4)
    page_no=request.GET.get('page')
    res['blg']=paginator.get_page(page_no)
    return render(request,'blog.html',res)

    
def blog_details(request):

    return render(request,'blog-detail.html')