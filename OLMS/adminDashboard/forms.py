from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from students.models import Book 


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class editUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
