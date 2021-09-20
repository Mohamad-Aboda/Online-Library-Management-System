from django.http import HttpResponse
from django.shortcuts import redirect

def unAuth_user(view_fun):
    def wrapper_fun(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_fun(request, *args, **kwargs)
    return wrapper_fun

def super():
    def decorator(view_func):
        def wrapper_fun(request, *args, **kwargs):
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')

        return wrapper_fun
    return decorator