from django.urls import path
from . import views

urlpatterns = [
    path('', views.diet_preferences, name='diet_preferences'),
]
