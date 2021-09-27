from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, editUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from shared.decorators import unAuth_user
from students.models import Book

@unAuth_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form' : form}
    return render(request, 'students/register.html', context)

@unAuth_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/adminPanel')
            else:
                return redirect('/student')
        else:
            pass
    return render(request, 'students/login.html')
    
def logoutUser(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/student/login')
def home(request):
    books = Book.objects.filter(status = request.user.username)
    img = Book.objects.filter(status = request.user.username)
    context = {'books':books, 'img':img}
    return render(request, 'students/home.html', context)

@login_required(login_url='/student/login')
def profile(request):
    username = request.user.username
    email = request.user.email
    firstName = request.user.first_name
    lastName = request.user.last_name
    context = {'username' : username, 'email' : email, 'firstName': firstName, 'lastName' : lastName}
    return render(request, 'students/profile.html', context)

@login_required(login_url='/student/login')
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
            return redirect('/student')
    context = {'form' : form}
    return render(request, 'students/editprofile.html', context)

