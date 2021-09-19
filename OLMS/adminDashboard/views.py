from django.http.response import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .forms import CreateUserForm, editUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import BookForm
from students.models import Book
#https://www.youtube.com/watch?v=tUqUdu0Sjyc&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=14&ab_channel=DennisIvy

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form' : form}
    return render(request, 'students/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/students')
        else:
            #ToDo
            pass
    return render(request, 'students/login.html')
    
def logoutUser(request):
    logout(request)
    return redirect('/students')

def home(request):
    return render(request, 'adminDashboard/home.html')

def profile(request):
    username = request.user.username
    email = request.user.email
    firstName = request.user.first_name
    lastName = request.user.last_name
    context = {'username' : username, 'email' : email, 'firstName': firstName, 'lastName' : lastName}
    return render(request, 'students/profile.html', context)

def editProfile(request):
    form = editUserForm()
    if request.method == 'POST':
        form = editUserForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            if not email:
                email = request.user.email
            firstName = request.POST['first_name']
            if not firstName:
                firstName = request.user.first_name
            lastName = request.POST['last_name']
            if not lastName:
                lastName = request.user.last_name
            password = request.POST['password1']
            user = User.objects.get(username=request.user)
            user.first_name = firstName
            user.last_name = lastName
            user.email = email
            user.set_password(password)
            user.save()
            logout(request)
            return redirect('/students')
    context = {'form' : form}
    return render(request, 'students/editprofile.html', context)



def addBook(request):
    form = BookForm()
    if request.method == "GET":
        context = {"form": form}
        return render(request, 'adminDashboard/addBook.html', context)

    if request.method == "POST":
        form = BookForm(request.POST)
        form.save()

    return redirect("homee")




def deleteBook(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect("homee")

def updateStudent(request, std_id):
    pass 
    
# def updateStudent(request, std_id):
#     student = get_object_or_404(Student, pk=std_id)
#     if request.method =="GET":
#         departments = Department.objects.all()

#         context={"student": student, "depts": departments}
#         return render(request, "students/editstudent.html", context)
#     if request.method =='POST':
#         mydept = Department.objects.get(pk=request.POST["dept"])

#         Student.objects.filter(pk=std_id).update(
#             name=request.POST["name"],
#             email=request.POST["email"],
#             img=request.POST["img"],
#             gender=request.POST["gender"],
#             dept=mydept)

#         return redirect("allstudents")


# def updateBook(request):
#     return render(request, 'adminDashboard/updateBook.html')
