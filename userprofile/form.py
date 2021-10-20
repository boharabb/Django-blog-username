from django import forms
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from django.db import models
from django.forms import fields

from userprofile.models import profile


class signupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class profileform(forms.ModelForm):
    class Meta:
        model = profile
        fields = ("phone", "bio", "address", "profileimage")


class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
