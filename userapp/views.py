from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'userapp/home.html', {'title': 'Welcome'})

def about(request):
    return render(request, 'userapp/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'userapp/contact.html', {'title': 'Contact'})
# Create your views here.

