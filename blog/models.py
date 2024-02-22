from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=75)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now) # auto_now_add=True means that the date will be added automatically when the post is created
    # defualt=timezone.now is used to set the date to the current date and time
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if the user is deleted, the post will be deleted as well
    # meaning the connection between the user and the post is one to many composition

    def __str__(self): # this is a dunder method that returns the title of the post when we query the database for the post 
        return self.title # only the title of the post will be returned
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) # this method will return the url of the post that was created
    
    # reverse vs redirect: reverse is used to return the url as a string while redirect is used to redirect the user to a specific url

    # if we want to redirect the user to the home page after creating a post, we can set an attribute called success_url in the PostCreateView class in views.py
    # success_url = '/' # this will redirect the user to the home page after creating a post