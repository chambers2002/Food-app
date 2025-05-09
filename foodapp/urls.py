from django.contrib import admin
from django.urls import path, include
from registration import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eco/', include('ecomeals.urls')),
    path('budget/', include('budgetgroceries.urls')),
    path('preferences/', include('dietpreferences.urls')),
    path('mealsuggestions/', include('mealsuggestions.urls')),
    path('', include('userapp.urls')),
    path('register/', views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
    path('profile', views.profile, name = 'profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)