from django.shortcuts import render

def meal_suggestions(request):
    recipes = []
    query = request.GET.get('query')
    if query:
        # Placeholder data (replace with API later)
        recipes = [
            {"title": f"{query.title()} Recipe 1", "image": "https://via.placeholder.com/150"},
            {"title": f"{query.title()} Recipe 2", "image": "https://via.placeholder.com/150"},
            {"title": f"{query.title()} Recipe 3", "image": "https://via.placeholder.com/150"},
        ]
    return render(request, "mealsuggestions/MealSuggestions.html", {"recipes": recipes})


# Create your views here.
