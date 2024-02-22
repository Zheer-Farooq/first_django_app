from django.contrib import admin

# Register your models here.

from .models import Profile

admin.site.register(Profile) # this will allow us to see the profile model in the admin page