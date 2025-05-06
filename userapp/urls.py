from django.urls import path
from . import views
from .views import MealRecommendationView

app_name = 'userapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('meals/', views.meals, name='meals'),
    path('api/recommendations/', MealRecommendationView.as_view(), name='meal-recommendations'),
]

