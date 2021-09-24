from django.db import models
from django.contrib.auth.models import AbstractUser


# This function used to define the path for content
def file_path(instance, file_name):

    return 'user_{0}/{1}'.format(instance.channel.id, file_name)


# Create your models here.
# User Model
class User(AbstractUser):
    pass


# Channel Model
class Channel(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name + 'by' + self.user.first_name



# Content Model
class Content(models.Model):

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    media = models.FileField(upload_to= file_path)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + ' on ' + self.channel.name


# Interaction 
class Interaction(models.Model):

    type = models.CharField(max_length=255)
    watch_time = models.IntegerField(null=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


# Comments
class Comment(models.Model):

    info = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    reply_ref = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)