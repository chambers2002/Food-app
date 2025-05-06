from django.urls import path
from . import views

app_name = 'mealsuggestions' 

urlpatterns = [
    path('', views.meal_suggestions, name='meal_suggestions'),
]
