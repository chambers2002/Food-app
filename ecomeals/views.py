import requests
from django.shortcuts import render

def eco_meals(request):
    eco_meals = []
    query = request.GET.get('eco_query')

    if query:
        url = f"https://world.openfoodfacts.org/cgi/search.pl"
        params = {
            "search_terms": query,
            "search_simple": 1,
            "action": "process",
            "json": 1,
            "page_size": 6
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json().get("products", [])
            eco_meals = [
                {
                    "product_name": item.get("product_name", "Unnamed"),
                    "image": item.get("image_url", ""),
                    "ecoscore": item.get("ecoscore_grade", "unknown"),
                    "nova": item.get("nova_group", "?"),
                    "nutriscore": item.get("nutriscore_grade", "?")
                }
                for item in results if item.get("product_name")
            ]
    
    return render(request, "ecomeals/EcoMeals.html", {"eco_meals": eco_meals})

def eco_meals_view(request):
    url = "https://world.openfoodfacts.org/cgi/search.pl?tagtype_0=categories&tag_contains_0=contains&tag_0=plant-based&json=1"
    response = requests.get(url).json()
    return render(request, 'eco_meals.html', {'products': response.get('products', [])})

