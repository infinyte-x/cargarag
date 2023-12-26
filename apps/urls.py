from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name="index" ),
    path('Packages/',Packages,name="Packages" ),
    path('about/',about,name="about" ),
    path('contact/',contact,name="contact" ),
    path('login/',login,name="login" ),
    path('emailus/',emailus,name="emailus" ),
    path('logout/',logout,name="logout" ),
    
]
