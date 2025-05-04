from django.urls import path
from . import views

urlpatterns = [
    path('', views.eco_meals, name='eco_meals'),
]
