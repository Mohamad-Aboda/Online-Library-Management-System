from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),
    path('details/<int:id>/', views.bookDetails, name='bookDetails'),
    path('borrowed/<int:id>', views.listAllBorrowedBooks, name='allBorrowedBooks'),


]
