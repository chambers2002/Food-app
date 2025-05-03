from django.shortcuts import render

def eco_meals(request):
    return render(request, 'ecomeals/EcoMeals.html')

def low_carbon(request):
    return render(request, 'ecomeals/LowCarbonMeals.html')

def low_waste(request):
    return render(request, 'ecomeals/LowWasteRecipes.html')

def local_ingredients(request):
    return render(request, 'ecomeals/LocalIngredientFinder.html')


# Create your views here.
