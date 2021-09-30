from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main.views import index, login_view, signUp, createChannel, channel_view, signout, uploadContent, video, interaction_status, feed_interaction

urlpatterns = [
    path('', index, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', signout, name='logout'),
    path('register/', signUp, name='register'),
    path('createChannel/', createChannel, name='createChannel'),
    path('channel/', channel_view, name='channel'),
    path('upload/', uploadContent, name='upload'),
    path('video/<int:video_id>/', video, name='video'),
    path('interaction-status/', interaction_status, name='interaction_status'),
    path('feed-interaction/', feed_interaction, name='feed_interaction')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)