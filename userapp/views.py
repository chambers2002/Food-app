from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'userapp/home.html', {'title': 'Welcome'})

def about(request):
    return HttpResponse('<h1>Hello this is our About page for our Food App</h1>')

def contact(request):
    return HttpResponse('<h1>Hello this is our Contact page for our Food App</h1>')
# Create your views here.

