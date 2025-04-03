from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello this is our home page for our Food App</h1>')
# Create your views here.

