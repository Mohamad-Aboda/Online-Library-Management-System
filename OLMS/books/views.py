from django.shortcuts import render
from django.http.response import HttpResponse

def books(request):
    return render(request, 'books/books.html')