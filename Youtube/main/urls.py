from os import name
from django.contrib import admin
from django.urls import path

from main.views import index, login_view, signUp, createChannel, channel_view

urlpatterns = [
    path('', index, name='home'),
    path('login/', login_view, name='login'),
    path('register/', signUp, name='register'),
    path('createChannel/', createChannel, name='createChannel'),
    path('channel/', channel_view, name='channel')
]