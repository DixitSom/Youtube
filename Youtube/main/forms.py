from django import forms

from .models import User, Channel


# This is form for user Login
class UserLoginForm(forms.ModelForm):

    email = forms.EmailField(max_length=20)
    password = forms.PasswordInput(render_value=False)

    class Meta:
        model = User
        fields = ['email', 'password']


# this form is for user Registration
class UserRegistrationForm(forms.ModelForm):

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=20)
    password = forms.PasswordInput()

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