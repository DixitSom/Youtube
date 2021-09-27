from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Content)
admin.site.register(Comment)
admin.site.register(Interaction)
admin.site.register(Channel)


