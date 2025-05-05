from django.shortcuts import render
import requests
from django.conf import settings

def diet_preferences(request):
    recipes = []
    diet = request.GET.get('diet','')
    allergies = request.GET.get('allergies', '')
    
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": settings.SPOONACULAR_API_KEY,
        "number": 6,
        "addRecipeNutrition": True,
    }
    
    if diet:
        params["diet"] = diet
    if allergies:
        params["intolerances"] = ','.join([a.strip().lower() for a in allergies.split(',')])
        
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            recipes = response.json().get("results", [])
        else:
            print("Error:", response.status_code, response.text)
    except Exception as e:
        print("API error:", str(e))
    
    return render(request, "dietpreferences/DietPreferences.html", {
        "recipes": recipes,
        "diet": diet,
        "allergies": allergies,
    })
    