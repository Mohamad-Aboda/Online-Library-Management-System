from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homee'),
    path('register', views.register, name="registerr"),
    path('login', views.loginPage, name="loginn"),
    path('logout', views.logoutUser, name="logoutt"),
    path('profile', views.profile, name="profilee"),
    path('editprofile', views.editProfile, name="editprofilee"),
    path('add/', views.addBook, name='addBook'),
    path("delete/<int:book_id>", views.deleteBook, name="deleteBook"),
    path("update/<int:book_id>", views.updateStudent, name="updateStudent"),


]
