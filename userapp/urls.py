from django.urls import path
from . import views

app_name = 'userapp'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('meals/', views.meals, name='meals'),
    path('mealsuggestions/', views.meal_suggestions, name='meal_suggestions'),
    path('budgetgroceries/', views.budget_groceries, name='budget_groceries'),
    path('dietpreferences/', views.diet_preferences, name='diet_preferences'),
    path('ecomeals/', views.eco_meals, name='eco_meals'),
]