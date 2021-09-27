from django.contrib import admin
from django.urls import path

from main.views import index, login_view, signUp

urlpatterns = [
    path('', index, name='home'),
    path('login/', login_view, name='login'),
    path('register/', signUp, name='register')
]