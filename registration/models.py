from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    
    def _str_(self):
        return f'{self.user.first_name} {self.user.last_name}'

# Create your models here.
