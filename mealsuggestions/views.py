from django.shortcuts import render

def meal_suggestions(request):
    return render(request, 'mealsuggestions/MealSuggestions.html')

def balanced_cards(request):
    return render(request, 'mealsuggestions/BalancedMealCards.html')

def student_meals(request):
    return render(request, 'mealsuggestions/StudentMealPlans.html')

def quick_easy(request):
    return render(request, 'mealsuggestions/QuickandEasy.html')


# Create your views here.
