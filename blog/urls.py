
from blog import views
from django.urls import path

urlpatterns = [



    path('blog/', views.blog,name='blog'),
    
    path('blog-detail/', views.blog_details,name='blog-detail'),
   
]
