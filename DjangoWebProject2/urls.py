from django.contrib import admin 
from django.urls import path,include

  

  
urlpatterns = [ 
    path('', include('APP1.urls')), 
    path('admin/', admin.site.urls), 
] 
      

