from django.shortcuts import render

def diet_preferences(request):
    filtered_meals = []
    diet = request.GET.get('diet')
    allergy = request.GET.get('allergy')
    if diet or allergy:
        # Placeholder meal suggestions
        filtered_meals = [
            {"title": f"{diet.title()} Friendly Meal 1"},
            {"title": f"{diet.title()} Friendly Meal 2"},
        ]
    return render(request, "dietpreferences/DietPreferences.html", {"filtered_meals": filtered_meals})


# Create your views here.
