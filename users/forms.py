from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() 

    class Meta: # This is a nested namespace for configurations and keeps the configurations in one place.
        model = User # This is the model that will be affected by this form.
        fields = ['username', 'email', 'password1', 'password2'] # This is the order in which the fields will be displayed in the form.

# This form will allow us to update the username and email of the user.
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta: # what is class Meta? It is a namespace that contains metadata options. It is a way to configure the behavior of the form.
        model = User
        fields = ['username', 'email']

# This form will allow us to update the profile picture of the user.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']