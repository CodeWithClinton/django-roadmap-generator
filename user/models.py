from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    passed = models.BooleanField(default=False)
    project = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length = 200, blank = True, null = True)
    last_name = models.CharField(max_length = 200, blank = True, null = True)
    username = models.CharField(max_length = 200, blank = True, null = True)
    image = models.ImageField(blank = True, null = True, upload_to = 'p_imgg')
    email = models.EmailField(blank=True, null=True)
    profession = models.CharField(max_length = 500, blank = True, null = True)
    bio  = models.TextField(blank = True, null = True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.user.username
