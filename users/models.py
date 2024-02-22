from django.db import models
from django.contrib.auth.models import User
from PIL import Image 
# Create your models here.
# we have a one to one relationship between the user and the profile 
# so it means that one user can have only one profile and one profile can have only one user

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # if the user is deleted then the profile will also be deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # python -m pip install Pillow
    # the above line will store the profile pictures in the profile_pics folder in the media directory of the project
    def __str__(self): # this is a dunder method which is used to return the string representation of the object
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # this will resize the image to 300x300
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.rotate(-90)
            img.save(self.image.path)