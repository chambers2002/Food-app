from django.shortcuts import render
import requests

def budget_groceries(request):
    location = request.GET.get('location', '')
    stores = []
    center = None
        
    if location:
        geo_url = "https://nominatim.openstreetmap.org/search"
        geo_params = {"q": location, "format": "json", "limit": 1}
        geo_res = requests.get(geo_url, params=geo_params, headers={"User-Agent": "budgergroceries-app"})
        
        if geo_res.status_code == 200 and geo_res.json():
            coords = geo_res.json()[0]
            lat = float(coords['lat'])
            lon = float(coords['lon'])
            center = {"lat": lat, "lon": lon}
            
            overpass_url = "http://overpass-api.de/api/interpreter"
            query = f"""
            [out:json];
            (
                node["shop"="supermarket"](around:1000,{lat},{lon});
                node["shop"="convenience"](around:1000,{lat},{lon});
                node["amenity"="fast_food"](around:1000,{lat},{lon});
            );
            out center 5;
            """
            res = requests.post(overpass_url, data=query)
            
            if res.status_code == 200:
                data = res.json()
                for element in data["elements"]:
                    name = element["tags"].get("name")
                    if name:
                        stores.append({
                            "name" : name,
                            "lat" : element["lat"],
                            "lon" : element["lon"]
                        })
            
    return render(request, "budgetgroceries/BudgetGroceries.html", {
        "location": location,
        "stores": stores[:5],
        "center": center
    })

