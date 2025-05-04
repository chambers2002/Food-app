from django.shortcuts import render

def eco_meals(request):
    eco_meals = []
    query = request.GET.get('eco_query')
    if query:
        # Placeholder data
        eco_meals = [
            {"title": f"Sustainable Meal with {query.title()} 1"},
            {"title": f"Sustainable Meal with {query.title()} 2"},
        ]
    return render(request, "ecomeals/EcoMeals.html", {"eco_meals": eco_meals})

# Create your views here.
