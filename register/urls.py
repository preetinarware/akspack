
from register import views
from django.urls import path

urlpatterns = [

    path('register/', views.usr_register,name='register'),
    
    path('login/', views.usr_login,name='login'),
    
    path('logout/', views.usr_logout,name='logout'),
    
    path('forgot-password/', views.frgt_pass,name='forgot-password'),
    
    path('password-confirm/<str:id>/',views.pwd_reset_cnfrm,name='pwd_cnfrm'),
    
    # path('register/', views.register,name='register'),
]
