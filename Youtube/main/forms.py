from django import forms
from django.db import models
from django.db.models import fields

from .models import Content, User, Channel, Comment


# This is form for user Login
class UserLoginForm(forms.Form):

    email = forms.CharField(max_length=20, widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)


# this form is for user Registration
class UserRegistrationForm(forms.ModelForm):

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

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
        exclude = ['user', 'created_at']


class ContentForm(forms.ModelForm):

    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    media = forms.FileField()
    tags = forms.CharField(max_length=100)

    class Meta:
        model = Content
        exclude = ['channel', 'user', 'created_at']


# Form for comments
class CommentForm(forms.ModelForm):

    # reply_ref = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Comment
        fields = ['info']