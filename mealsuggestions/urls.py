from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_suggestions, name='meal_suggestions'),
]
