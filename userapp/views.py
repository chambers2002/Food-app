from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
import sendgrid
from sendgrid.helpers.mail import Mail
from .forms import ContactForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionnaireSerializer

def home(request):
    return render(request, 'userapp/home.html', {'title': 'Welcome'})

def about(request):
    return render(request, 'userapp/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'userapp/contact.html', {'title': 'Contact'})

def meals(request):
    return render(request, 'userapp/meals.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
            content = f"From: {name} <{email}>\n\n{message}"
            mail = Mail(
                from_email=settings.DEFAULT_FROM_EMAIL,
                to_emails='yourdestination@example.com',
                subject='Submission for New Contact Form',
                plain_text_content=content
            )
            try:
                sg.send(mail)
                messages.success(request, 'Successful Message')
                return redirect('contact')
            except Exception as e:
                messages.error(request, f'Error sending message: {e}')
    else:
        form = ContactForm()
    return render(request, 'userapp/contact.html', {'form': form})

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
