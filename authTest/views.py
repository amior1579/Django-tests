from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *


def home(request):
    return render(request, 'authTest/index.html',{
        
    })


def login(request):
    return render(request, 'authTest/login.html',{
        
    })

def register(request):
    return render(request, 'authTest/register.html',{

    })


def user_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        username_exists = UserAuth.objects.values_list('username', flat=True)
        
        if confirmation != password:
            return render(request, 'authTest/register.html',{
                'message': ' !رمز عبور مطابقت ندارد, لطفا دوباره وارد کنید',
            })  
        elif username in username_exists is not None:
            return render(request, 'authTest/register.html',{
                'username_exists_message': 'کاربری با این نام کاربری از قبل وجود دارد',
            })  
        else:
            user = UserAuth.objects.create_user(username,password)
            user.save()
            return HttpResponseRedirect(reverse('home'))
        
    else:
        return render(request, 'authTest/register.html')
