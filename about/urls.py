
from about import views
from django.urls import path

urlpatterns = [

    path('about/', views.about,name='about'),
    
    path('contact/', views.contact,name='contact'),
   
]
