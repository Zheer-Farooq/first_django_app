# this is used to create a profile for each user when they are created
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# **kwargs is used to accept any additional keyword arguments passed to the function
# what is **kwargs? https://www.geeksforgeeks.org/args-kwargs-python/

# The @receiver decorator connects the create_profile function to the post_save signal of the User model
# The create_profile function receives the signal and creates a Profile instance for each new User instance
@receiver(post_save, sender=User) # when a user is saved, send the signal to the receiver
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# The save_profile function saves the Profile instance
# kwargs just accepts any extra keyword arguments passed to the function
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
