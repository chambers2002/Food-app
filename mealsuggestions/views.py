import requests
from django.conf import settings
from django.shortcuts import render

def meal_suggestions(request):
    recipes = []
    query = request.GET.get('query')

    if query:
        api_key = settings.SPOONACULAR_API_KEY  # Load from settings
        url = "https://api.spoonacular.com/recipes/complexSearch"
        params = {
            "query": query,
            "number": 6,
            "addRecipeInformation": True,
            "apiKey": api_key,
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            recipes = response.json().get("results", [])
    
    return render(request, "mealsuggestions/MealSuggestions.html", {"recipes": recipes})
