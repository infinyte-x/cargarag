from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def index(request):
    return render(request,"index.html")
def Packages(request):
    return render(request,"Packages.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def login(request):
    email=request.POST.get("email")
    passw=request.POST.get("password")
    if request.method=="POST":
       user=auth.authenticate(username=email,password=passw)
       if user is not None:
            auth.login(request,user)
            return redirect(index) 
       else:
            return render(request,"login.html",{'error_login':"Invalide User and Password"})
    
    return render(request,"login.html")
def emailus(request):
    return render(request,"emailus.html")
def logout(request):
    auth.logout(request)
    return redirect(index)
