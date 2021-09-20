from django.shortcuts import render
from students.models import Book
# Create your views here.


def landingpage(request):
    books = Book.objects.all()
    img = Book.objects.all()
    context = {'books':books, 'img':img}
    return render(request, "shared/landingpage.html", context)

def about(request):
	return render(request, 'shared/about.html')

def contact(request):
	return render(request, 'shared/contact.html')


