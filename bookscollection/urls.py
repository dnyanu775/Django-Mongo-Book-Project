"""
URL configuration for bookscollection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('login/',views.login),
    path('loginpage/',views.loginpage),
    path('home/login.html/',views.loginpage),
    path('home/Register.html/',views.registerpage),
    path('adduser/',views.register),
    path('home/index.html',views.home),
    path('searchbook/',views.searchbook),
    path('searchbookonid/',views.searchbookonid),
    path('searchid',views.searchid),
    path('adminpage/',views.adminpage),
    path('addbook/',views.addbook),
    path('addbookpage/',views.addbookpage),
    path('deletebook/',views.deletebook),
    path('allbooks/',views.all_books),
    path('searchforupdate/',views.searchforupdate),
    path('searchupdatebookonid/',views.searchupdatebookonid),
    path('updateform/',views.updateform),
    path('update/',views.update),
    
]
