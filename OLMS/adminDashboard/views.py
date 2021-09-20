from django.shortcuts import get_object_or_404, render, redirect
from . forms import BookForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from shared.decorators import super
from students.models import Book

#https://www.youtube.com/watch?v=tUqUdu0Sjyc&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=14&ab_channel=DennisIvy

@login_required(login_url='/students/login')
@super()
def home(request):
    return render(request, 'adminDashboard/home.html')

@login_required(login_url='/students/login')
@super()
def addBook(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        form.save()
    context = {"form": form}
    return render(request, 'adminDashboard/addBook.html', context)

@login_required(login_url='/students/login')
@super()
def updateBook(request):
	return render(request, 'adminDashboard/updateBook.html')

@login_required(login_url='/students/login')
@super()
def DeleteBook(request):
    books = Book.objects.all()
    img = Book.objects.all()
    context = {'books':books, 'img':img}
    return render(request, "adminDashboard/deleteBook.html", context)

@login_required(login_url='/students/login')
@super()
def delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect("adminPanel")

@login_required(login_url='/students/login')
@super()
def update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES,  instance = book)
        form.save()
    context = {"book":book.title, "form": form}
    return render(request, "adminDashboard/updateBook.html", context)

@login_required(login_url='/students/login')
@super()
def allstudents(request):
    User = get_user_model()
    users = User.objects.all()
    context = {'users' : users}
    print(context)
    return render(request, "adminDashboard/allstudents.html", context)

@login_required(login_url='/students/login')
@super()
def student(request, student_id):
    try:
        user = User.objects.get(id=student_id)
        context = {
            "found" : 1,
            "username" : user.username,
            "id" : user.id,
            "email" : user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_superuser" : user.is_superuser
        }
    except:
        context = {
            "found" : 0
        }
    return render(request, "adminDashboard/student.html", context)

@login_required(login_url='/students/login')
@super()
def allbooks(request):
    books = Book.objects.all()
    img = Book.objects.all()
    context = {'books':books, 'img':img}
    return render(request, "adminDashboard/allbooks.html", context)

@login_required(login_url='/students/login')
@super()
def borrowedbooks(request):
    books = Book.objects.filter(status__isnull=False)
    img = Book.objects.filter(status__isnull=False)
    context = {'books':books, 'img':img}
    return render(request, "adminDashboard/borrowedbooks.html", context)