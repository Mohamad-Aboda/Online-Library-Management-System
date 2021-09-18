from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/register', views.register, name="register"),
    path('/login', views.loginPage, name="login"),
    path('/logout', views.logoutUser, name="logout"),
    path('/', views.home, name="home"),
]
