from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'first_name','last_name','email','profile_pic']
        location=  forms.ModelChoiceField(queryset=Location.objects.all())

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','email']