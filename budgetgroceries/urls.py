from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_groceries, name='budget_groceries'),
]