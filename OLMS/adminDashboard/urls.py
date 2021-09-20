from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='adminPanel'),
    path('add/', views.addBook, name='addBook'), 
    path("delete/", views.DeleteBook, name="deleteBook"),
    path("delete/<int:book_id>", views.delete, name="delete"),
    path("update/<int:book_id>", views.update, name="update"),
    path("allstudents", views.allstudents, name="allstudents"),
    path("student/<int:student_id>", views.student, name="student"),
    path("allbooks", views.allbooks, name="allbooks"),
    path("borrowedbooks", views.borrowedbooks, name="borrowedbooks"),
    
]
