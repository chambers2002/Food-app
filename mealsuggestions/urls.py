from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_suggestions, name='meal_suggestions'),
    path('BalancedMealCards/', views.balanced_cards, name='balanced_cards'),
    path('StudentMealPlans/', views.student_meals, name='student_meals'),
    path('QuickandEasy/', views.quick_easy, name='quick_easy'),
]