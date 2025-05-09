from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created for {username}! Now you can login!')
            return redirect('userapp:home')
        else: 
            messages.warning(request, 'You are unable to create an Account')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html',
                  {'form': form, 'title': 'Student Registration'})

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'title': 'Student Profile'})
# Create your views here.
