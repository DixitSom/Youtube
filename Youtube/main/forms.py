from django import forms
from django.db import models
from django.forms import fields

from .models import User, Channel


# This is form for user Login
class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']


# this form is for user Registration
class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


# this is form is used to create Channels
class ChannelForm(forms.ModelForm):

    class Meta:
        model = Channel
        exclude = ['user']