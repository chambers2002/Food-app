from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'userapp/home.html', {'title': 'Welcome'})

def about(request):
    return render(request, 'userapp/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'userapp/contact.html', {'title': 'Contact'})

def meals(request):
    return render(request, 'userapp/meals.html', {'title': 'Meals'})

def meal_suggestions(request):
    return render(request, 'userapp/mealsuggestions.html')

def budget_groceries(request):
    return render(request, 'userapp/budgetgroceries.html')

def diet_preferences(request):
    return render(request, 'userapp/dietpreferences.html')

def eco_meals(request):
    return render(request, 'userapp/ecomeals.html')

# Create your views here.

