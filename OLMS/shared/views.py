from django.shortcuts import render, get_object_or_404
from students.models import Book
import datetime
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

def bookDetails(request, id):
    bookDetails = get_object_or_404(Book, pk=id)
    return render(request, 'shared/details.html', {'bookDetails':bookDetails})



def listAllBorrowedBooks(request, id):
    # bookStatus = Book.objects.filter(user=request.user)
    bookStatus = get_object_or_404(Book, pk=id)
    bookStatus.status = 1
    bookStatus.return_date = datetime.datetime.now() + datetime.timedelta(days=10)
    bookStatus.save()

    allBorrowedBooks = Book.objects.filter(status = 1)
    return render(request, 'shared/allBorrowedBooks.html', {'allBorrowedBooks':allBorrowedBooks})


# def returnBook(request):
#     bookStatus = get_object_or_404(Book, pk=id)
#     bookStatus.status = None 
#     bookStatus.return_date = None 
#     bookStatus.save()
#     return render(request, 'shared/allBorrowedBooks.html')



