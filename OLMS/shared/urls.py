from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),
    path('details/<int:id>/', views.bookDetails, name='bookDetails'),
    path('borrow/<int:id>', views.confirmBorrow, name='borrow'),
    path('borrowed/<int:id>/<slug:date>', views.borrowed, name='borrowed'),
    path('return/<int:id>', views.returnBook, name="returnBook"),
]
