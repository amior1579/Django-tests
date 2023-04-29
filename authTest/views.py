from django.shortcuts import render, redirect


def home(request):
    return render(request, 'authTest/index.html',{
        
    })


def login(request):
    return render(request, 'authTest/login.html',{
        
    })

def register(request):
    return render(request, 'authTest/register.html',{

    })