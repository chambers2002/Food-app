from django.shortcuts import render

def diet_home(request):
    return render(request, 'dietpreferences/DietPreferences.html')

def custom_diet(request):
    return render(request, 'dietpreferences/CustomDietPlans.html')

def allergy_tracker(request):
    return render(request, 'dietpreferences/AllergyTracker.html')

def recommended_meals(request):
    return render(request, 'dietpreferences/RecommendedMeals.html')

def diet_settings(request):
    return render(request, 'dietpreferences/DietFilterSettings.html')


# Create your views here.
