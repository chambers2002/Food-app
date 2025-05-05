from django.urls import path
from . import views

app_name = 'userapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('meals/', views.meals, name='meals'),
]

#NEED TO CHANGE THESE INTO URLS.PY PAGE