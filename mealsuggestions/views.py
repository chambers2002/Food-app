import requests
from django.conf import settings
from django.shortcuts import render

def meal_suggestions(request):
    query = request.GET.get('query', '')
    recipes = []
    if not query:
        recipes = [
        {
            "title": "Simple Grilled Chicken Bowl",
            "id": 716426,
            "image": "https://spoonacular.com/recipeImages/716426-312x231.jpg"
        }
    ]
    query = request.GET.get('query')
    cheap = request.GET.get ('cheap')
    max_calories = request.GET.get('max_calories')

    if query:
        api_key = settings.SPOONACULAR_API_KEY
        url = "https://api.spoonacular.com/recipes/complexSearch"
        params = {
            "query": query,
            "addRecipeInformation": True,
            "number": 6,
            "apiKey": api_key
        }

        if max_calories:
            params["maxCalories"] = max_calories
        if cheap:
            params["tags"] = "cheap"

        response = requests.get(url, params=params)
        if response.status_code == 200:
            recipes = response.json().get("results", [])

    return render(request, "mealsuggestions/MealSuggestions.html", {
        "recipes": recipes,
        "query": query,
        "cheap": cheap,
        "max_calories": max_calories
    })
