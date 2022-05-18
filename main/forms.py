from pyexpat import model
from django import forms
from .models import Room
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Topic

class RoomcreationForm(forms.ModelForm):
    class Meta:
        model=Room
        fields=["title","topic","description"]
        

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1"]