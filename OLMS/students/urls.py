from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name="register"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('profile', views.profile, name="profile"),
    path('editprofile', views.editProfile, name="editprofile"),
]
