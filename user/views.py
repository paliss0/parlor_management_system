from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
# Create your views here.

def user_login(req):
    if req.method=="GET":
        return render(req,'login.html')
    else:
        username=req.POST['username']
        password=req.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(req,user)
            return redirect('parlor_home')
        else:
            return redirect('login')

def sign_up(req):
    if req.method=="GET":
        return render(req,'sign-up.html')
    else:
        username=req.POST['username']
        password=req.POST['password']
        email=req.POST['email']

        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()

        return redirect('login')

def user_logout(req):
    logout(req)
    return redirect ('login')
    
