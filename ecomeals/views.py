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
            # Filter to only items with eco info
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


# Create your views here.
