from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import Profile
 
 
@receiver(post_save, sender=settings.AUTH_USER_MODEL) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, username=instance.username, email=instance.email)
  
@receiver(post_save, sender=Profile) 
def update_user(sender, instance, **kwargs):
        user = instance.user 
        user.username = instance.username 
        user.email = instance.email 
        user.save()