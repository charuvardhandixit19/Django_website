from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
     path("",views.index,name="home"),  
     path("about",views.about,name="about"),  
     path("contact",views.contact,name="contact"), 
     path("services",views.services,name="services"),  
 
]


admin.site.site_header = "Frosty Treats Delight Admin"
admin.site.site_title = "Frosty Treats Delight Admin Portal"
admin.site.index_title = "Welcome to Frosty Treats Delight Portal"

