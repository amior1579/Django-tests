from django.urls import path
from . import views

urlpatterns = [
    # urls
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),

    # server request
    path('user_registration', views.user_registration, name='user_registration'),


]