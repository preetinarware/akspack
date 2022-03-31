from django.contrib import admin
from django.urls import path,include
from admin_dashboard import views

urlpatterns = [
    
  path('', views.ad_dash, name='ad_dash'),
  
  path('Messages/', views.cont, name='cont'),
  # path('admin-register/', views.ad_register, name='ad_register'),
  path('admin-login/', views.ad_login, name='ad_login'),
  
  
  path('password-change/<str:id>/', views.pwd_reset_change, name='pwd_reset_change'),
  path('admin-logout/', views.ad_logout, name='ad_logout'),
  path('admin-reset-password/', views.ad_forgot_pwd, name='ad_forgot_pwd'),

  path('admin-profile/', views.ad_profile, name='ad_profile'),

  path('add-product/', views.add_product, name='add_product'),
  path('product-detail/', views.ad_product, name='ad_product'),
  
  path('product-uses/', views.prod_uses, name='prod_uses'),
  
  path('product-coupon/', views.prod_coupn, name='prod_coupn'),
  path('product-size/', views.prod_size, name='prod_size'),
  
  path('product-style-&-category/', views.style_cate, name='style_cate'),
  path('product-thickness-&-material/', views.thick_mtrial, name='thick_mtrial'),

  path('page-not-found/', views.error404, name='404'),
  path('transactions/', views.payments, name='payments'),
  path('product-price/', views.pric, name='price'),





  
  path('Page-not-found/', views.error404, name='error'),
  # path('profile-details/<slug:stud>', views.stud_detail, name='stud_detail'),

  
  # path('event-detail/', views.ad_event, name='ad_event'),
  # path('course-detail/', views.ad_crs, name='ad_course'),
  # path('blog-detail/', views.ad_blogs, name='ad_blog'),
  # path('instrucor-detail/', views.inst, name='inst'),
  # path('student-detail/', views.stud, name='stud'),
  
  # path('add-blog/', views.add_blog, name='add_blog'),
  # path('add-course/', views.add_crs, name='add_crs'),
  # path('add-event/', views.add_event, name='add_event'),
  # path('profile-detail/', views.detail, name='detail'),

  
  # path('product-detail/', views.ad_product, name='ad_product'),
  # path('product-detail/', views.ad_product, name='ad_product'),
  # path('product-detail/', views.ad_product, name='ad_product'),
  # path('product-detail/', views.ad_product, name='ad_product'),
  # path('product-detail/', views.ad_product, name='ad_product'),


  
]
