from django.shortcuts import render
from students.models import Book
# Create your views here.


def landingpage(request):
    books = Book.objects.all()
    pic = Book.objects.all()
    context = {'books':books, 'pic':pic}
    return render(request, "shared/landingpage.html", context)


def deleteBook(request, std_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect("homee")



def about(request):
	return render(request, 'shared/about.html')


def contact(request):
	return render(request, 'shared/contact.html')


