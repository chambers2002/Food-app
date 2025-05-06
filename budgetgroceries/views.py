from django.shortcuts import render
import requests

def budget_groceries(request):
    location = request.GET.get('location','')
    stores = []
    
    if location:
        geo_url = "https://nominatim.openstreetmap.org/search"
        geo_params = {"q": location, "format": "json", "limit": 1}
        geo_res = requests.get(geo_url, params=geo_params, headers={"User-Agent": "budgergroceries-app"})
        
        if geo_res.status_code == 200 and geo_res.json():
            coords = geo_res.json()[0]
            lat, lon = float(coords['lat']), float(coords['lon'])
            
            stores = [
                {"name": "Grocery Student Discounts", "lat": lat + 0.001, "lon": lon + 0.001},
                {"name": "Express Budget Marketing", "lat": lat - 0.001, "lon": lon - 0.001}
            ]
            
    return render(request, "budgetgroceries/BudgetGroceries.html", {
        "location": location,
        "stores": stores
    })

def budget_groceries_view(request):
    max_price = request.GET.get('max_price')  
    return render(request, 'budget_groceries.html', {'max_price': max_price})
