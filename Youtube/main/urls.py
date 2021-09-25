from main.views import login_view
from django.contrib import admin
from django.urls import path

from main.views import index

urlpatterns = [
    path('', index, name='home'),
    path('login/', login_view, name='login')
]