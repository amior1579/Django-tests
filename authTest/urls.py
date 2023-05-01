from django.urls import path
from . import views

urlpatterns = [
    # urls
    path('', views.home, name='home'),
    path('login_page', views.login_page, name='login_page'),
    path('register_page', views.register_page, name='register_page'),
    path('logout_user', views.logout_user, name='logout_user'),

    # server request
    path('user_registration', views.user_registration, name='user_registration'),


]