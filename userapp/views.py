from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
import sendgrid
from sendgrid.helpers.mail import Mail
from .forms import ContactForm

def home(request):
    return render(request, 'userapp/home.html', {'title': 'Welcome'})

def about(request):
    return render(request, 'userapp/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'userapp/contact.html', {'title': 'Contact'})

def meals(request):
    return render(request, 'userapp/meals.html', {'title': 'Meals'})

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


