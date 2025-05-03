from django.urls import path
from . import views

urlpatterns = [
    path('EcoMeals/', views.eco_meals, name='eco_meals'),
    path('LowCarbonMeals/', views.low_carbon, name='low_carbon'),
    path('LowWasteRecipes/', views.low_waste, name='low_waste'),
    path('LowerIngredientFinder/', views.local_ingredients, name='local_ingredients'),
]
