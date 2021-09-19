from django.shortcuts import render

# Create your views here.


def landingpage(request):
	return render(request, 'shared/landingpage.html')

def about(request):
	return render(request, 'shared/about.html')


def contact(request):
	return render(request, 'shared/contact.html')