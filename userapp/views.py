from django.shortcuts import render, redirect
from django.conf import settings
from userapp.forms import ContactForm
from .forms import ContactForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionnaireSerializer
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'userapp/home.html', {'title': 'Welcome'})

def about(request):
    return render(request, 'userapp/about.html', {'title': 'About'})

@login_required
def meals(request):
    return render(request, 'userapp/meals.html')

def planner_page(request):
    return redirect("https://spoonacular.com/meal-planner")

def food_article(request):
    return redirect("https://spoonacular.com/articles")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            EmailMessage(
                'Student Contact Submission from {}'.format(name),
                message,
                'form-response@example.com',
                ['declanchambers666@gmail.com'],
                reply_to=[email]
            ).send()
            return redirect ('userapp:success')
    else:
        form = ContactForm()        
    return render(request, 'userapp/contact.html', {'form': form})
    
def success(request):
    return render(request, 'userapp/success.html')

class MealRecommendationView(APIView):
    def post(self, request):
        serializer = QuestionnaireSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Extract user inputs
        preferences = serializer.validated_data.get('preferences', [])
        allergies = serializer.validated_data.get('allergies', [])
        budget = serializer.validated_data.get('budget')
        eco_friendly = serializer.validated_data.get('eco_friendly', False)
        max_calories = serializer.validated_data.get('max_calories')
        
        redirect_url = self._get_redirect_url(preferences, allergies, budget, eco_friendly, max_calories)
        return Response({'redirect_url': redirect_url})    
    
    def _get_redirect_url(self, preferences, allergies, budget, eco_friendly, max_calories):
        if eco_friendly:
            return "/eco/"
        
        if allergies:
            allergy_tags = ','.join(allergies)
            return f"/mealsuggestions/?exclude_allergens={allergy_tags}"

        if preferences:
            diet = preferences[0]
            return f"/preferences/?filter={diet}"

        if budget:
            return f"/budget/?max_price={budget}"

        diet = preferences[0] if preferences else "chicken"
        return f"/mealsuggestions/?query={diet}&cheap=true&max_calories={max_calories or 600}"
    
    
    
    
