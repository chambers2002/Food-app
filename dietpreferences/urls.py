from django.urls import path
from . import views

urlpatterns = [
    path('DietPreferences/', views.diet_home, name='diet_home'),
    path('CustomDietPlans/', views.custom_diet, name='custom_diet'),
    path('AllergyTracker/', views.allergy_tracker, name='allergy_tracker'),
    path('RecommendedMeals/', views.recommended_meals, name='recommended_meals'),
    path('DietFilterSettings/', views.diet_settings, name='diet_settings'),
]