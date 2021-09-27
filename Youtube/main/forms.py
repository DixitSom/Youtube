from django import forms
from django.forms import Widget

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
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        # widgets = {
        #     f: Widget(attrs={'required':'required'}) for f in fields
        # }


# this is form is used to create Channels
class ChannelForm(forms.ModelForm):

    class Meta:
        model = Channel
        exclude = ['user']