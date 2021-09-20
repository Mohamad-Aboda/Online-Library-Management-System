from django.shortcuts import redirect, render, get_object_or_404
from students.models import Book
from .forms import ContactForm

def landingpage(request):
    books = Book.objects.all()
    img = Book.objects.all()
    context = {'books':books, 'img':img}
    return render(request, "shared/landingpage.html", context)

def about(request):
    return render(request, 'shared/about.html')

def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    context = {'form': form}
    return render(request, 'shared/contact.html', context)

def bookDetails(request, id):
    bookDetails = get_object_or_404(Book, pk=id)
    return render(request, 'shared/details.html', {'bookDetails':bookDetails})



def confirmBorrow(request, id):
    bookDetails = get_object_or_404(Book, pk=id)
    return render(request, 'shared/borrow.html', {'bookDetails':bookDetails})

def borrowed(request, id, date):
    bookStatus = get_object_or_404(Book, pk=id)
    bookStatus.status = request.user.username
    date = date.split('-')
    day = date[1]
    month = date[0]
    year = date[2]
    date = year + '-' + month + '-' + day
    bookStatus.return_date = date
    bookStatus.save()
    return redirect('/')




def returnBook(request, id):
    bookStatus = get_object_or_404(Book, pk=id)
    bookStatus.status = None
    bookStatus.return_date = None
    bookStatus.save()
    return redirect('/student')