from django.urls import path
from . import views
from .views import MealRecommendationView
from userapp.views import contact, success, planner_page, food_article

app_name = 'userapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
    path('meals/', views.meals, name='meals'),
    path('api/recommendations/', MealRecommendationView.as_view(), name='meal-recommendations'),
    path('planner/', planner_page, name='planner_page'),
    path('foodarticle/', food_article, name='food_article'),
]

