from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_home, name='budget_home'),
    path('CheapStaples/', views.cheap_staples, name='cheap_staples'),
    path('WeeklyDeals/', views.weekly_deals, name='weekly_deals'),
    path('BudgetCalculator/', views.budget_home, name='budget_home'),
    path('StoreComparison/', views.store_comparison, name='store_comparison'),
]