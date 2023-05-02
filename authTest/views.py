from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .serializers import *


def home(request):
    return render(request, 'authTest/index.html',{
        
    })


def login_page(request):
    return render(request, 'authTest/login.html',{
        
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'authTest/login.html',{
                'login_message':'نام کاربری و یا رمز عبور نامعتبر است'
            })

def register_page(request):
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



def logout_user(request):
    logout(request)

    return redirect('home')



# API
@csrf_exempt
def users_api(request):
        user_auth = UserAuth.objects.all()
        if request.method == 'GET':
            # print(user_auth)
            serializer = UserSerializer(user_auth, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({"error": "GET or PUT request required."}, status=400)
