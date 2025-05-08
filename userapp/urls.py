from django.urls import path
from . import views
from .views import MealRecommendationView
from userapp.views import contact, success

app_name = 'userapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
    path('meals/', views.meals, name='meals'),
    path('api/recommendations/', MealRecommendationView.as_view(), name='meal-recommendations'),
]

