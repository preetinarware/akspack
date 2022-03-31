
from shop import views
from django.urls import path

urlpatterns = [

    path('product/', views.product,name='product'),
    
    path('cart/', views.cart,name='cart'),
    
    path('checkout/', views.checkout,name='checkout'),
    
    path('product-detail/', views.product_detail,name='product-detail'),
    
    # path('register/', views.register,name='register'),
]
