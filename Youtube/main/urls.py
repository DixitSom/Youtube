from django.urls import path

from main.views import index, login_view, signUp, createChannel, channel_view, signout, uploadContent

urlpatterns = [
    path('', index, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', signout, name='logout'),
    path('register/', signUp, name='register'),
    path('createChannel/', createChannel, name='createChannel'),
    path('channel/', channel_view, name='channel'),
    path('upload', uploadContent, name='upload')
]