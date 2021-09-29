from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main.views import index, login_view, signUp, createChannel, channel_view, signout, uploadContent, video

urlpatterns = [
    path('', index, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', signout, name='logout'),
    path('register/', signUp, name='register'),
    path('createChannel/', createChannel, name='createChannel'),
    path('channel/', channel_view, name='channel'),
    path('upload/', uploadContent, name='upload'),
    path('video/<int:video_id>/', video, name='video')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)